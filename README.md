# ylab-fastapi-postgresql-docker

## To start this app do the following steps:


1. Измените ```".env"``` для ваших переменных окружения

Например, для запуска основного приложения:

```bash
DB_HOST=postgres_db
DB_PORT=5432
DB_NAME=ylabproject
DB_USER=postgres
DB_PASS=root

REDIS_HOST=redis_db
REDIS_PORT=6379
REDIS_DB=0
```

Для запуска тестов:
```bash
DB_HOST=test_postgres_db
DB_PORT=5432
DB_NAME=menutest
DB_USER=postgres
DB_PASS=root

REDIS_HOST=test_redis_db
REDIS_PORT=6379
REDIS_DB=1
```
2. Запустите приложение
```bash
docker-compose up -d
```
4. Запустите тесты
```bash
docker-compose -f "docker-compose.tests.yml" up
```
