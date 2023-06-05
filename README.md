# yamdb_final
![Deploy badge](https://github.com/belikrastr/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
### Описание
API позволяет пользователям добавлять отзывы о фильмах, книгах и музыке, а также получать рейтинги для произведений.
### Технологии
- Python 
- Django 
- Django REST Framework
- Gunicorn
- Nginx
- Docker
- Github-Actions
- Postgresql
- Actions

### Подготовка к запуску проекта
- Склонировать репозиторий на локальную мшину
```bash
git clone git@github.com:belikrastr/yamdb_final.git
```
- Cоздайте .env файл в директории yamdb_final/infra/ и впишите:
```python
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Запуск проекта в контейнере
- Запустите docker-compose:
```
docker-compose up -d --build
```
```
docker-compose up
```
- Выполните миграции:
```
docker-compose exec web python manage.py migrate
```
- Создайте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
- Соберите статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
- Ссылка на развернутый проект http://localhost/redoc/

### Примеры запросов к API.

- Регистрация пользователя и получение confirmation_code
###
POST http://localhost/api/v1/auth/signup/
Content-Type: application/json
```js
{
    "email": "user@mail.ru",
    "username": "user"
}
```

- Получение токена пользователя
###
POST http://localhost/api/v1/auth/token/
Content-Type: application/json
```js
{
    "username": "user2",
    "confirmation_code": "65y-64a6e988500b2eeac0b"
}
```
- Получить данные своей учетной записи
###
GET  http://localhost/api/v1/users/me/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4OTQ4Njc1LCJqdGkiOiJjYmE4NGMzZGUzYjI0ODA5OTY3ZjJiODZiOTM2YjQzYiIsInVzZXJfaWQiOjV9.guSbTtW-YBKsmOYzwzE7xu0tPXQ7dMoI2YzbAi4ZSw8


- Изменить данные своей учетной записи
###
PATCH http://localhost/api/v1/users/me/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4ODA0ODU3LCJqdGkiOiIyZjEzZWMzZWM1MDU0ODI0OTU1ZmUwM2Y4MmE2NDU2NSIsInVzZXJfaWQiOjV9.bzQTBMpOjztnhLwo-rXGQXY7eqwzyX23XtqkMq0f22U
Content-Type: application/json
```js
{
    "username": "user2",
    "email": "user2@mail.ru",
    "first_name": "User",
    "last_name": "user",
    "bio": "",
    "role": "user"
}
```

- Получение списка всех пользователей с токеном Админа
###
GET   http://localhost/api/v1/users/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4ODc3NTUzLCJqdGkiOiJmOGI5NDNhMjY5Mjk0MWNkOGQzZmQyYzk4N2JlODljOSIsInVzZXJfaWQiOjJ9.rw69vzp1RU80K-2PHiGPjRVm3umj0cKCaAy5ulZ7xJc
Content-Type: application/json


- Получаем token admin
###
POST http://localhost/api/v1/auth/token/
Content-Type: application/json
```js
{
    "username": "admin"
}
```

### Автор проекта
Беликов Владимир - [Telegram](https://t.me/belikrastr) - belikrastr@yandex.ru

Project Link: [https://github.com/belikrastr/yamdb_final](https://github.com/belikrastr/yamdb_final)
