# 📖 Evently (Django)

Система бронирования мероприятий с поддержкой:
- аутентификации пользователей
- email-оповещений
- интеграции с Telegram-ботом
- импорта событий (ручного и автоматического)

## 🔍 Структура проекта

```
event_booking/
├── manage.py
├── event_booking/         # Настройки Django
├── users/                 # Регистрация, логин, Telegram-профиль
├── events/                # Модели мероприятий, ручной ввод, админка
├── booking/               # Бронирование мероприятий, логика статусов
├── bot_api/               # Интеграция с Telegram-ботом через API
├── event_importer/        # Импорт событий из внешних источников
└── templates/             # HTML-шаблоны
```

## 🌐 Установленные приложения (INSTALLED_APPS)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users',           # Пользователи и профили
    'events',          # Мероприятия
    'booking',         # Бронирование
    'bot_api',         # Telegram API
    'event_importer',  # Парсеры и импорты событий
]
```

## 🏢 Назначение приложений

### 1. `users`
- Регистрация / вход / выход
- Подтверждение email
- Хранение Telegram-юзернейма
- Профиль пользователя

### 2. `events`
- Модель `Event`
- Ручное добавление и редактирование мероприятий
- Отображение списка событий с фильтрацией
- Админка для управления событиями

### 3. `booking`
- Модель `Booking`
- Уникальность бронирования по пользователю и событию
- Контроль доступных билетов
- Email-уведомление о бронировании
- Отмена и просмотр бронирований

### 4. `bot_api`
- REST API для Telegram-бота
- Получение списка событий через чат
- Возможность бронирования и получения уведомлений в Telegram

### 5. `event_importer`
- Импорт событий из внешних источников (RSS/API/HTML)
- Автоматическое добавление/обновление записей `Event`
- Управление источниками (`EventSource` модель)
- Отметка `source = 'import'` для отслеживания

## ✉️ Интеграции

### Email
- Используется SMTP через Gmail или другой почтовый сервис
- Подтверждение регистрации
- Уведомления о бронировании событий

### Telegram
- Подключение Telegram-бота через `python-telegram-bot` или Webhook
- Пользователь связывает аккаунт с ботом по username
- Оповещения в Telegram о бронированиях и напоминания

## 📊 Возможности

- ✅ Регистрация/вход пользователей
- ✅ Просмотр и фильтрация мероприятий
- ✅ Онлайн-бронирование мест
- ✅ Email-подтверждение и Telegram-уведомления
- ✅ Ручной и автоматический ввод событий
- ✅ Административная панель управления

## 🚀 Новые возможности (22.05.2025)

- ✅ Выбор количества билетов при бронировании (с учётом остатка)
- ✅ Нельзя забронировать одно и то же событие дважды (уникальность бронирования)
- ✅ В профиле пользователя отображаются все его бронирования (название, дата, количество билетов)
- ✅ В деталях события поле "Правила" поддерживает HTML (картинки, форматирование)
- ✅ На главной отображаются все события, включая прошедшие (фильтрация по дате опциональна)

## 📚 Как начать

### 📥 Клонируйте репозиторий
git clone <repo_url>

### 🧠 Откройте проект в PyCharm:
 File → Open → Выберите папку проекта

### 🛠️ Создайте виртуальное окружение (если PyCharm не предложит автоматически):
 File → Settings → Project: <имя проекта> → Python Interpreter → Add → Virtualenv

 ✅ Убедитесь, что выбран Python 3.10+

### 📦 Установите зависимости:
pip install -r requirements.txt

### 🔄 Примените миграции:
python manage.py migrate

### 👤 Создайте суперпользователя:
python manage.py createsuperuser

### ▶️ Запустите сервер:
python manage.py runserver

### 🌐 Перейдите в браузере:
http://127.0.0.1:8000
