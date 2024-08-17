# Lesson_DJ01. Введение в Django и создание проекта.

---

# Django Проект с Главной Страницей и Страницами Data и Test

## Описание

Этот проект создан на Django и включает в себя три страницы:
1. **Главная страница (`/`)** - Содержит ссылки на страницы `/data` и `/test`.
2. **Страница Data (`/data`)** - Отображает простое сообщение на странице.
3. **Страница Test (`/test`)** - Тестовая страница с другим содержимым.

## Установка

1. Клонируйте репозиторий или скопируйте файлы проекта на свой компьютер:

    ```bash
    git clone <URL_РЕПОЗИТОРИЯ>
    cd <ИМЯ_ПАПКИ_ПРОЕКТА>
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # На Windows: venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции базы данных:

    ```bash
    python manage.py migrate
    ```

5. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

6. Откройте в браузере:

    ```bash
    http://127.0.0.1:8000/
    ```

## Структура проекта

- `myapp/` - Основное Django приложение, содержащее логику проекта.
- `myapp/views.py` - Файл, содержащий функции представлений для обработки запросов.
- `myapp/templates/myapp/index.html` - Шаблон главной страницы.

## Маршруты

- `/` - Главная страница со ссылками на другие страницы.
- `/data/` - Страница с сообщением "Это страница с данными".
- `/test/` - Тестовая страница с сообщением "Это тестовая страница".

## Шаблон index.html

Шаблон `index.html` содержит ссылки на страницы `/data` и `/test`, которые генерируются с помощью встроенной Django функции `{% url %}`.

## Дополнительная информация

Проект является простым примером использования Django для создания страниц и маршрутизации между ними. Он может быть использован как основа для разработки более сложных приложений.

 
