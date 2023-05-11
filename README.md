# yamdb_final
![Deploy badge](https://github.com/belikrastr/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
### Описание
API позволяет пользователям добавлять отзывы о фильмах, книгах и музыке, а также получать рейтинги для произведений.
### Технологии
Python 3.7
Django 2.2.19
Django REST Framework 3.12.4
Django REST Framework Simple JWT 4.7.2
### Запуск проекта 
- Запустите docker-compose:
```
docker-compose up -d --build
```
```
docker-compose up
```
- Создайте новые файлы миграций:
```
docker-compose exec web python manage.py makemigrations users
```
```
docker-compose exec web python manage.py makemigrations reviews
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
- Зайдите на http://localhost/redoc/ и создайте запись
### Авторы
Владимир
