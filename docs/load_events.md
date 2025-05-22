# Загрузка событий из KudaGo API с помощью команды `populate_events`

## 📌 Описание

Команда `populate_events` — это Django management-команда, предназначенная для импорта мероприятий из KudaGo Public API в базу данных проекта. Используется для автоматического обновления событий по расписанию или вручную.

## ⚙️ Что делает код

- Получает список жанров (`genres`) и городов (`cities`) из KudaGo и сохраняет их в модели `Genre` и `City`
- Загружает события постранично (до 100 штук за раз)
- Для каждого события:
  - определяет город, жанр, место проведения (`Location`)
  - создает или обновляет объект `Event` с данными
  - сохраняет изображение события (если есть)
- Обновление происходит без дублирования за счёт `external_id`

---

## 🧪 Тестирование

1. Убедитесь, что в `events/models.py` определены следующие модели с нужными полями:
   - `Event`: содержит `external_id`, `city`, `location`, `genre`, `ticket_price`, `event_date`, `start_time`, `image` и др.
   - `City`, `Genre`, `Location` — модели со связями
2. Убедитесь, что приложение `events` добавлено в `INSTALLED_APPS` в `settings.py`:

```python
   INSTALLED_APPS = [
       ...,
       'events',
   ]
````

3. Создайте структуру Django-команды:

   ```
   events/
   └── management/
       └── commands/
           └── populate_events.py
   ```

   Все каталоги (`management`, `commands`) должны содержать пустой `__init__.py`.

4. Выполните миграции (если вносились изменения в модели):

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Запустите команду вручную (см. ниже)

---

## 🖐 Как запускать вручную

Выполните команду из корня проекта:

```bash
python manage.py populate_events
```

Пример вывода:

```
Fetching genre mappings...
Genre mapping loaded.
Populating cities...
Successfully populated 6 cities
Populating genres...
Successfully populated 21 genres
Populating events...
Created event: Ночь музеев 2025
Event already exists: Выставка на ВДНХ
Finished populating events
```

---

## ⏱️ Как запускать по расписанию (CRON)

1. Откройте crontab:

   ```bash
   crontab -e
   ```

2. Добавьте строку для запуска команды, например каждые 6 часов:

   ```bash
   0 */6 * * * /path/to/venv/bin/python /absolute/path/to/manage.py populate_events >> /var/log/populate_events.log 2>&1
   ```

   Где:

   * `/path/to/venv/bin/python` — путь до Python внутри виртуального окружения
   * `/absolute/path/to/manage.py` — абсолютный путь до `manage.py` проекта
   * `>>` — добавляет лог вывода в файл `/var/log/populate_events.log`

---

## 📝 Примечания

* Убедитесь, что в `settings.py` корректно настроены `MEDIA_URL` и `MEDIA_ROOT`, если изображения событий сохраняются через `ImageField`.
* При необходимости, можно создать отдельную команду `cleanup_events`, удаляющую старые или устаревшие записи.
* Не забудьте добавить проверку на корректность загружаемых данных, если будете расширять команду.
