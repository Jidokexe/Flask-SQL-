### 🐳 Flask + PostgreSQL + Nginx с Docker Compose

## 📌 Описание
Этот проект демонстрирует развертывание простого REST API-приложения на Flask, подключенного к базе данных PostgreSQL, с проксированием запросов через Nginx, используя Docker Compose.

API предоставляет два маршрута:

GET / — базовый маршрут для проверки доступности приложения.

GET /users — возвращает список пользователей из базы данных в формате JSON.

🛠️ Стек технологий
Flask — веб-фреймворк Python.

PostgreSQL — реляционная СУБД.

SQLAlchemy — ORM для Flask.

Nginx — веб-сервер и прокси.

Docker и Docker Compose — контейнеризация и оркестрация.

## 📁 Структура проекта
bash
Копировать
Редактировать
.
├── app.py                  # Flask-приложение
├── requirements.txt        # Python-зависимости
├── Dockerfile              # Docker-образ для Flask
├── docker-compose.yml      # Compose-файл для всех сервисов
├── nginx.conf              # Конфигурация Nginx
└── README.md               # Документация проекта

## 🚀 Быстрый старт
🔃 Предварительные требования
Docker

Docker Compose

▶️ Запуск проекта
Клонируйте репозиторий:

bash
Копировать
Редактировать
git clone https://github.com/your-username/flask-postgres-docker.git
cd flask-postgres-docker
Постройте и запустите проект:

bash
Копировать
Редактировать
docker-compose up --build
Приложение будет доступно по адресу:

arduino
Копировать
Редактировать
http://localhost

## 🌐 API-документация
GET /
Проверка работоспособности.

Пример ответа:

text
Копировать
Редактировать
Hello, World!
GET /users
Возвращает всех пользователей из базы данных PostgreSQL.

Пример ответа:

json
Копировать
Редактировать
[
  { "id": 1, "name": "Alice" },
  { "id": 2, "name": "Bob" }
]

## ⚠️ При первом запуске база будет пустой, и маршрут /users вернёт пустой массив: [].

## ⚙️ Конфигурация
Переменные окружения (настраиваются в docker-compose.yml):
PostgreSQL (сервис db):
yaml
Копировать
Редактировать
POSTGRES_DB=usersdb
POSTGRES_USER=user
POSTGRES_PASSWORD=password
Flask (сервис flask):
yaml
Копировать
Редактировать
DATABASE_URL=postgresql://user:password@db:5432/usersdb
db — имя сервиса базы данных, по которому Flask подключается внутри Docker-сети.

## 💾 Хранение данных
Для сохранения данных между перезапусками используется Docker volume:

yaml
Копировать
Редактировать
volumes:
  - pgdata:/var/lib/postgresql/data
Том pgdata хранит данные PostgreSQL независимо от жизни контейнеров.

## 🛑 Остановка и очистка
Остановка всех контейнеров:
bash
Копировать
Редактировать
docker-compose down
Полное удаление контейнеров и данных:
bash
Копировать
Редактировать
docker-compose down -v

## 📌 Примечания
База данных создаётся автоматически при первом запуске контейнера PostgreSQL.

Таблица User создаётся через SQLAlchemy, как только Flask-приложение стартует.

Приложение прослушивает порт 5000 внутри контейнера, но доступно через Nginx на http://localhost.

## 📱 Контактная информация
Email: IvanilovVM22@st.ithub.ru Telegram: @Jidok_exe
