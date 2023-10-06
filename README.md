# Описание.
## API в рамках учебного проекта «Yatube».
Данное API предоставляет возможность получать посты, группы, комментарии 
и подписки с сайта «Yatube».
# Установка.
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/94R1K/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
```

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

# Примеры работы API:

### GET-запрос на получение постов:

```
http://127.0.0.1:8000/api/v1/posts/
```

### Ответ от API:

```json
{
    "count": 7,
    "next": "http://127.0.0.1:8000/cats/?limit=2&offset=6",
    "previous": "http://127.0.0.1:8000/cats/?limit=2&offset=2",
    "results": [
        {
            "id": 5,
            "name": "Пончик",
            "color": "Mixed",
            "birth_year": 2019,
            "achievements": [
                {
                    "id": 1,
                    "achievement_name": "уронил вазу"
                },
                {
                    "id": 2,
                    "achievement_name": "напал из-за угла"
                }
            ],
            "owner": 1,
            "age": 2
        },
        {
            "id": 6,
            "name": "Марсель",
            "color": "Mixed",
            "birth_year": 2019,
            "achievements": [
                {
                    "id": 1,
                    "achievement_name": "уронил вазу"
                },
                {
                    "id": 2,
                    "achievement_name": "напал из-за угла"
                }
            ],
            "owner": 1,
            "age": 2
        }
    ]
}
```

### POST-запрос для добавления комментария к публикации:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

```json
{
  "text": "string"
}
```

### Ответ от API:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
# Об авторе
Лошкарев Ярослав Эдуардович \
Python-разработчик (Backend) \
Россия, г. Москва \
E-mail: real-man228@yandex.ru 

[![VK](https://img.shields.io/badge/Вконтакте-%232E87FB.svg?&style=for-the-badge&logo=vk&logoColor=white)](https://vk.com/yalluv)
[![TG](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/yallluv)
