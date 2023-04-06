## Описание:

Данный проект является подобием социальной сети для создания постов и групп, а так же подписки на авторов и отслеживании их активности.

Из проекта исключили фронтенд и view-функции приложения posts. Остался только API сервис


## Примеры запросов API:

### Запрос:

*Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.*

**POST** http://127.0.0.1:8000/api/v1/posts/
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
### Ответ:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
### Запрос:

*Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.*

**POST** http://127.0.0.1:8000/api/v1/follow/
```
{
  "following": "string"
}
```
### Ответ:
```
{
  "user": "string",
  "following": "string"
}
```
### Запрос:

*Получение комментария к публикации по id.*

**GET** http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
### Ответ:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
### Запрос:

*Получение информации о сообществе по id.*

**GET** http://127.0.0.1:8000/api/v1/groups/{id}/
### Ответ:
```
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Kulikov1/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
