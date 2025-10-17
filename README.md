# API для Дневника на FastAPI и PostgreSQL

Это RESTful API для простого приложения-дневника, созданное с использованием FastAPI. Приложение и его база данных (PostgreSQL) полностью контейнеризированы с помощью Docker и управляются через Docker Compose.

## 🚀 Технологии

- **Бэкенд**: FastAPI
- **База данных**: PostgreSQL
- **ORM**: SQLAlchemy
- **Валидация данных**: Pydantic
- **Контейнеризация**: Docker, Docker Compose
- **Асинхронный драйвер БД**: asyncpg

## ✅ Основные возможности

- Полный набор CRUD-операций для записей в дневнике.
- Асинхронная работа с базой данных.
- Готовая среда для запуска в Docker.

## 📋 Требования

Для запуска проекта на вашем компьютере должны быть установлены:

- **[Docker](https://www.docker.com/get-started)**
- **[Docker Compose](https://docs.docker.com/compose/install/)** (устанавливается вместе с Docker Desktop)

## ⚙️ Установка и запуск

Следуйте этим шагам, чтобы запустить проект локально.

#### 1. Скачайте docker-compose.yml

#### 2. Настройте переменные окружения

Для работы приложения необходимы переменные окружения. Создайте файл `.env` в корневой директории проекта и заполните его следующим образом.

```
# Конфигурация базы данных

POSTGRES_USER=app_user

POSTGRES_PASSWORD=secret_pass

POSTGRES_DB=diary_db

POSTGRES_HOST=db

POSTGRES_PORT=5432

  

# Полный URL для FastAPI

DATABASE_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

  

# Порт для FastAPI

APP_PORT=8000
```
При необходимости можете просто скопировать содержимое в свой `.env` файл.

### 3. Запустите проект с помощью Docker Compose

```
docker compose up
```

- Чтобы остановить и удалить контейнеры, используйте `docker compose down`.

## 🚀 Использование API

После успешного запуска:

- **API будет доступен по адресу**: `http://localhost:8000` (или по порту, который вы указали в `APP_PORT`).
- **Интерактивная документация (Swagger UI)**: `http://localhost:8000/docs`.

Через Swagger UI вы можете тестировать все эндпоинты прямо в браузере.
