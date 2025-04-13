# Куда пойти?

Интерактивная карта Москвы, на которой отмечаются виды отдыха с подробным описанием и комментариями локации.

![image](https://github.com/user-attachments/assets/e7639fc1-3478-48d3-92b0-edf2bdcf0368)


## Особенности
Благодаря удобной админ-панели администратор может быстро указывать данные о локации (включая загрузку фотографий), а так же опубликовывать их на карту.

Возможность редактирования существующих записей.

Встроенный в админку редактор позволяет красиво редактировать подробное описание локации.

![image](https://github.com/user-attachments/assets/2d2be50a-6336-4a38-b653-9788708f7ec7)

Пример JSON с данными:
```javascript
{
    "title": "Водопад Радужный",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7252a5cbb831eec01d98f3c234f2dfc5.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/c0191d876a75c05d72d9845251758b34.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/3daa4472d29bc5e3c82a62edb7ea6cfe.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b6bd1cb01af50fa7ab1ffd09ac7b0f58.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/17cf1ed6097edcf70824e87c414ed420.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b6a19f8f3daa32bdf904c1d7bf80f940.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6cc194af04b385b4b439dab0f81ebdda.jpg"
    ],
    "description_short": "Центральная Россия — край водопадов! Не верите? А зря.",
    "description_long": "<p>Вас привлекает романтика природы? Горные ручьи и водопады грезятся во снах и видениях, а до отпуска ещё как до луны? Не переживайте: всего в сорока пяти километрах от столицы вас ждёт удивительное природное творение — водопад Радужный. Ради него стоит прокатиться по Калужской автостраде практически до населённого пункта Папино, затем повернуть направо около моста через речку Нару возле заправочной станции, а там — после монумента героям Великой Отечественной войны по просёлочному тракту метров тридцать, и вы уже слышите манящий шум падающей воды.</p><p>Ваша настойчивость будет щедро вознаграждена. Крутая излучина реки Нара открывает взору удивительную долину семи ключей. Пробившись из-под земли, они сливаются в один мощный поток, который срывается с обрыва высотой в несколько метров. Радуга играет в брызгах чистейшей ледяной воды, а дальше с густо покрытого мхом берега стекают ручейки поменьше и совсем крошечные, образующие каскад уровнем ниже.</p><p>Проведите день в таком месте, побродите под сенью деревьев, усладив свой взор и слух, и вы со спокойной душой доживёте до ближайшего отпуска.</p>",
    "coordinates": {
        "lng": "36.940988",
        "lat": "55.20653999999999"
    }
}
```
Для быстрой загрузки данных в БД воспользуйтесь командой:

```bash
python manage.py load_place <link_to_json>
```

Где `<link_to_json>` - ссылка на исходный код JSON файла, пример которого представлен выше. Пример ссылки на JSON [файл](https://raw.githubusercontent.com/devmanorg/where-to-go-places/refs/heads/master/places/%D0%90%D1%80%D1%82-%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%BE%20%C2%AB%D0%91%D1%83%D0%BD%D0%BA%D0%B5%D1%80%20703%C2%BB.json). Если используете GitHub: выберите файл, откройте его на отдельной странице и нажмите кнопку Raw. Так вы получите ссылку на исходный код файла.
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
STATIC_ROOT = static/
MEDIA_URL = /media/
MEDIA_ROOT = media/
```
Ниже приведены ссылки на официальную документацию Django по переменным окружения:
* [SECRET_KEY](https://docs.djangoproject.com/en/5.2/ref/settings/#secret-key)
* [DEBUG](https://docs.djangoproject.com/en/5.2/ref/settings/#debug)
* [ALLOWED_HOSTS](https://docs.djangoproject.com/en/5.2/ref/settings/#allowed-hosts)
* [STATIC_URL](https://docs.djangoproject.com/en/5.2/ref/settings/#static-url)
* [STATIC_ROOT](https://docs.djangoproject.com/en/5.2/ref/settings/#static-root)
* [MEDIA_URL](https://docs.djangoproject.com/en/5.2/ref/settings/#media-url)
* [MEDIA_ROOT](https://docs.djangoproject.com/en/5.2/ref/settings/#media-root)

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

Демо-версия [сайта](https://bukadimka2342341.pythonanywhere.com/)

## Цель проекта

Код написан в образовательных целях.
