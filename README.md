# Telegram-бот с API сервисом

## Описание

Этот проект представляет собой Telegram-бота который взаимодействует только с зарегистрированными,
авторизованными пользователями, которые в свою учётную запись подключили бота с API сервисом для регистрации,
получения токена, авторизации и подключения бота.

## Используемые технологии

*   Python
*   Aiogram
*   FastApi
*   Pydantic
*   PostgreSQL
*   Docker

## 🛠 Установка и запуск (через Docker)

1.  Клонируйте репозиторий: `git clone https://github.com/Dim-Aks/FastApiBot.git`
2. Создайте файл `.env` и заполните его:
    ```
    SECRET_KEY = "YOUR_SECRET_KEY"
    TELEGRAM_BOT_TOKEN='YOUR_TELEGRAM_BOT_TOKEN'
    POSTGRES_USER='YOUR_POSTGRES_USER'
    POSTGRES_PASSWORD='YOUR_POSTGRES_PASSWORD.'
    POSTGRES_DB='YOUR_POSTGRES_DB'
    DATABASE_URL = "DATABASE_URL=postgresql://user:password@db:5432/dbname"
    ```
3. Соберите и запустите контейнер: `docker-compose up --build`
4. Дождитесь запуска сервисов.

## Использование 

Открываем доку http://127.0.0.1:8000/docs/

* `POST /register`: Регистрация нового пользователя.
* `POST /token`: Аутентификация пользователя и получение токена доступа.
*  После получения токена необходимо авторизоваться (справа вверху будет доступное расширение).
* `GET /users/me`: Получение информации о пользователе.
*  Пишем в телеграмм бота `/start` и получаем свой **telegram_id**.
* `PUT /telegram_id`: Подключение Telegram бота к аккаунту пользователя (потребуется **telegram_id**).
*  Теперь телеграм-бот будет отвечать вам на любой введённый текст суммой символов.

### 📬 Контакты
**Дмитрий**

Telegram: @Dim_Ax