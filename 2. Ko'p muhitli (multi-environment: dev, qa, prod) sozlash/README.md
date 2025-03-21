# Best practices for multi-environment Django project with Docker Compose

This guide covers essential DevOps and Django-related topics for handling environment variables, configuring services, managing Docker containers, and ensuring service reliability.

## Topics Covered

### 1. Install and configure poetry
- [x] Why poetry?
- [x] Configure Poetry in Dockerfile
- [x] Install dependencies in Dockerfile or entrypoint.sh
- [x] Difference between installing dependencies in Dockerfile and entrypoint.sh

<details><summary>Help guide</summary>

```commandline
pip install poetry
poetry init
poetry add Django
poetry add pytest --group test
```

Configure Poetry in Dockerfile:
```commandline
# Install Poetry
RUN apt clean && apt update && apt install curl netcat vim -y
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app/
```

Install dependencies:
```commandline
poetry install --without dev --no-root
```

</details>

### 2. Separate settings for testing and live environments

Source: [Django Settings: Best Practices](https://code.djangoproject.com/wiki/SplitSettings)

- [x] Configure `defaults.py`, `live.py`, and `testing.py` files
- [x] Load settings based on the environment
- [x] Read environment variables in Django settings with `decouple`
- [x] Manage `.env` files for testing and live environments
- [x] Read environment variables from different .env files in docker-compose.yml

<details><summary>Help guide</summary>

```commandline
├── settings
│   ├── defaults.py
│   ├── __init__.py
│   ├── live.py
│   └── testing.py
```
**Example environment files structure:**
```
# testing environments
.env.local
.env.test

# live environments
.env.dev
.env.qa
.env.prod
```

**Example `.env.example` file:**
```ini
SECRET_KEY=supersecretkey
DB_ENGINE=django.db.backends.postgresql
DB_NAME=demo_db
DB_USER=demo_user
DB_PASS=demo_pass
DB_HOST=localhost
DB_PORT=5432
```

**Loading environment variables in Django (`settings.py`):**
```python
from decouple import Config, RepositoryEnv
config = Config(RepositoryEnv(BASE_DIR / ".env"))

DEBUG = config("DEBUG", default=False, cast=bool)
SECRET_KEY = config(
    "SECRET_KEY",
    default="/aeEkzQCgomr]DnyS-i/0,kz!ZYWU>Z3#294@",
)
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASS"),
        "HOST": config("DB_HOST"),
    }
}
```
</details>

### 3. Configuring Redis in Django Settings and Docker Compose

- [x] Install Redis in Django
- [x] Configure Redis in Django settings
- [x] Add Redis service in Docker Compose

<details><summary>Help guide</summary>

**Installing Redis in Django:**
```bash
poetry add django-redis
```

**Configure in Django settings**
```python
REDIS_HOST = config("REDIS_HOST", default="localhost")
REDIS_PORT = config("REDIS_PORT", default=6379)
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
```

**Docker Compose configuration (`docker-compose.yml`):**
```yaml
services:
  redis:
    container_name: ${ENVIRONMENT-dev}-redis
    image: redis:7-alpine
    restart: always
    expose:
      - "6379"
```

</details>


### 4. Installing Packages in Dockerfile

- [x] Install packages in Dockerfile
- [x] how to use netcat (`nc`) in entrypoint.sh

<details><summary>Help guide</summary>

**Optimized Dockerfile example:**
```dockerfile
FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 # Prevents Python from writing pyc files
ENV PYTHONUNBUFFERED=1 # Prevents Python from buffering stdout and stderr

RUN apt clean && apt update && apt install curl netcat vim -y
```

**Waiting for PostgreSQL to be ready before starting Django:**
```sh
if [ "$DB_ENGINE" = "django.db.backends.postgresql" ]; then
  echo "Waiting for postgres..."
  while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
  done
  echo "PostgreSQL started"
fi
```
</details>

### 5. Improve Docker Compose Services

- [x] Configure network in Docker Compose
- [x] Configure health checks for services
- [x] Configure restart policy for services

<details><summary>Help guide</summary>

```yaml
services:
  web:
    container_name: ${ENVIRONMENT-dev}-app
    restart: always
    image: ${ENVIRONMENT-dev}-app:latest
    build:
        context: ..
        dockerfile: Dockerfile
    env_file:
      - ../source/.env.${ENVIRONMENT-dev}
    environment:
      - ENVIRONMENT=${ENVIRONMENT-dev}
    ports:
      - "${SVC_PORT-8000}:${SVC_PORT-8000}"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    networks:
      network:
  db:
    container_name: ${ENVIRONMENT-dev}-db
    image: postgres:15-alpine
    restart: always
    expose:
      - "5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER:-demo_user} -d ${DB_NAME:-demo_db}"]
      interval: 10s
      timeout: 5s
      retries: 5
    environment:
      - POSTGRES_USER=${DB_USER-demo_user}
      - POSTGRES_PASSWORD=${DB_PASS-demo_pass}
      - POSTGRES_DB=${DB_NAME-demo_db}
    volumes:
      - db-data:/var/lib/postgresql/data:rw
    networks:
      network:
  redis:
    container_name: ${ENVIRONMENT-dev}-redis
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    restart: always
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      network:

networks:
  network:
    name: ${ENVIRONMENT-dev}-network
```

</details>
