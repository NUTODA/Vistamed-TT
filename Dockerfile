FROM python:3.11-slim

# Установка зависимостей, необходимых для asyncpg
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копирование wait-for-it.sh
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Копирование зависимостей и установка
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

CMD ["/usr/local/bin/wait-for-it.sh", "db:5432", "--timeout=30", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]