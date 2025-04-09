# Куда пойти?

Интерактивная карта Москвы, на которой отмечаются виды отдыха с подробным описанием и комментариями локации.

ДОБАВИТЬ ФОТКУ САЙТА!!!!!

## Особенности
Благодаря удобной админ-панели администратор может быстро указывать данные о локации (включая загрузку фотографий), а так эе опубликовывать их на карту.

Возможность редактирования существующих записей.

Встроенный в админку редактор позволяет красиво редактировать подробное описание локации.

ДОБАВИТЬ ФОТО!!!!!

## Требования

- Python 3.7+
- Django 5.1+
- Установленные зависимости из `requirements.txt`

## Установка

1. Клонируйте репозиторий:

```bash
git https://github.com/Hard-Working-Dimka/where_to_go
```

2. Создайте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

4. Создайте файл для переменных окружения в корне проекта `.env`. Переменные окружения:

```
SECRET_KEY = 
```
Ниже представлены переменные окружения, которые имеют значения по умолчанию. При необходимости можно устанавливать на свои.
```
DEBUG = True
ALLOWED_HOSTS = *
STATIC_URL = /static/'
STATICFILES_DIRS = static/
STATIC_ROOT = media/
MEDIA_URL = /media/
MEDIA_ROOT = media/
```

5. Примените миграции базы данных:

```
python manage.py migrate
```

6. Создайте суперпользователя для доступа к административной панели:

```
python manage.py createsuperuser
```

7. Запустите сервер разработки:

```
python manage.py runserver
```
## Админ-панель

Панель администратора доступна по [адресу](http://127.0.0.1:8000/admin/) для управления всеми моделями.

## Демо-версия сайта

Данные в картах взяты из [репозитория](https://github.com/devmanorg/where-to-go-places).

ДОБАВИТЬ ДЕМКУ САЙТА!!!!
## Цель проекта

Код написан в образовательных целях.