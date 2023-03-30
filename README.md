<h2 align="center">Movie_project</h2>

### Описание проекта
Киноайт с фильмами, актерами/режиссерами, поиском, регистрацией, пагинацией, отзывами

- Категории
- Жанры
- Фильмы
- Кадры из фильма
- Режиссеры\Актеры
- Звезды рейтинга
- Отзывы
- Фильтры

**Стек**
- Python >= 3.10
- Django >= 4.1.7
- sqlite3

Установка

pip install req.txt

Старт

python manage.py runserver

## Разработка
#### 1) Поставить звездочку)
#### 2) Клонировать репозиторий
git clone https://github.com/True-Ha/Django_Cinema_site.git

#### 3) Создать виртуальное окружение
cd kino_project

python -m venv venv
#### 4) Активировать виртуальное окружение
Linux:
source venv/bin/activate
Windows:
./venv/Scripts/activate
#### 5) Устанавливить зависимости:
pip install -r req.txt
#### 6) Выполнить команду для выполнения миграций
python manage.py migrate
#### 8) Создать суперпользователя
python manage.py createsuperuser
#### 9) Запустить сервер
python manage.py runserver
#### 10) Ссылки
Сайт http://127.0.0.1:8000/

Админ панель http://127.0.0.1:8000/admin

