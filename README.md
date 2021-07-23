# Тестовое задание для ДомКлик

**Проверена работа в Python 3.8.7**

Используется: **SQLite, Django, DRF, pytest, django-telegrambot**

## УСТАНОВКА

1. Склонировать репозиторий

`git clone https://github.com/mikepro-alfamail-ru/domclick.git`

2. Перейти в папку с проектом

`cd domclick`

3. Установить virtual environment

`python -m venv <%venv_dir%>
`
4. И активировать

```
Платформа    Шелл       Команда для активации виртуального окружения

POSIX	     bash/zsh	$ source <venv>/bin/activate
             fish	    $ . <venv>/bin/activate.fish
             csh/tcsh   $ source <venv>/bin/activate.csh
PowerShell   Core       $ <venv>/bin/Activate.ps1
Windows      cmd.exe    C:\> <venv>\Scripts\activate.bat
PowerShell   PS         C:\> <venv>\Scripts\Activate.ps1
```

5. Установить необходимые пакеты

`pip install -r requirements.txt`
или 

`pip install requirements-dev.txt` для поддержки тестов

6. Для работы телеграм бота необходимы токен и имя бота.

Создать файл settings_local.py и внести в него токен

`tg_token = '<%bot_token%>'`

7. Провести миграции

`python manage.py migrate`

8. Для тестирования можно загрузить пробные данные в БД

`python manage.py loaddata requests.json`

9. Создать суперпользователя

`python manage.py createsuperuser`

Токен суперпользователя создастся автоматически

9. Запустить проект

`python manage.py runserver`

10. Телеграм бот работает в режиме POLLING

`python manage.py botpolling --username=<%bot_name%>`

11. Для получения токена суперпользователя можно воспользоваться админкой, либо POST запросом к api `http://127.0.0.1:8000/api-token-auth/?username=<%username%>&password=<%password%>`

## Тесты

1. Установить переменную среды `DJANGO_SETTINGS_MODULE=domclick.settings`

2. `pytest`

## Описание API

Для доступа ко всем функиям API используется авторизация по токену

`Authorization: Token <%superuser_token%>`

### Ресурсы

#### api/v0/staff - Сотрудники

Методы:

- GET - получить список сотрудников

возможно указать параметры для поиска `name` и `email`

Пример:

```
GET {{baseUrl}}/api/v0/staff/
Authorization: Token {{admintoken}}
```

(Примеры здесь и далее из VSCode)

Пример ответа:

```
[
  {
    "id": 1,
    "name": "John Rembo",
    "email": "qwe@as.sa"
  }
]
```

- POST - создать сотрудника. Обязательные поля: `name`

Пример:
```
POST {{baseUrl}}/api/v0/staff/
Authorization: Token {{admintoken}}
Content-Type: application/json

{
  "name": "John Rembo444",
  "email": "qwe@as.sa"
}
```

- PATCH - изменить сотрудника

Пример:

```
PATCH {{baseUrl}}/api/v0/staff/1/
Authorization: Token {{admintoken}}
Content-Type: application/json

{
  "name": "Another Staff Name"
}
```

- DELETE - удалить сотрудника

Пример:

```
DELETE {{baseUrl}}/api/v0/staff/1/
Authorization: Token {{admintoken}}
Content-Type: application/json

```

#### api/v0/customers - Пользователи

Использование аналогично staff

#### api/v0/requests - Заявки

Пример:

```
[
  {
    "id": 1,
    "title": "Test title",
    "description": "",
    "status": "CLOSED",
    "created_at": "2021-07-22T20:08:37.632000Z",
    "updated_at": "2021-07-23T21:16:04.887986Z",
    "customer": 1,
    "staff": 1
  },
  {
    "id": 2,
    "title": "Test title",
    "description": "",
    "status": "OPEN",
    "created_at": "2021-07-23T21:15:57.639827Z",
    "updated_at": "2021-07-23T21:15:57.639827Z",
    "customer": 1,
    "staff": null
  }
]
```

Обязательные поля: `title, customer, status`. Поле `status` при создании автоматически устанавливается в **OPEN**

Возможные статусы: **OPEN**, **IN WORK**, **CLOSED**

Методы:

- GET 

```
GET {{baseUrl}}/api/v0/requests/
Authorization: Token {{admintoken}}
```
  
(пример ответа выше)

- POST

Пример:
```
POST {{baseUrl}}/api/v0/requests/
Authorization: Token {{admintoken}}
Content-Type: application/json

{
  "title": "Test title",
  "customer": 1
}
```

- PATCH

```
PATCH {{baseUrl}}/api/v0/requests/1/
Authorization: Token {{admintoken}}
Content-Type: application/json

{
  "status": "CLOSED",
  "staff": 1
}
```

- DELETE

```
DELETE {{baseUrl}}/api/v0/requests/1/
Authorization: Token {{admintoken}}
```


### Работа телеграм бота

Для запуска оповещений пользователь должен отправить боту команду `/start <%my_email%>`, где my_email - адрес, который указан в БД.

После этого id чата сохраняется для данного пользователя. При изменении статуса заявок в чат отправляется сообщение.
