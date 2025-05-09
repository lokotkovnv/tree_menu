# Tree Menu
Проект реализует древовидное меню для Django-проекта в виде отдельного приложения (menu)

## Возможности
Древовидная структура меню любой вложенности  
Поддержка нескольких разных меню на одной странице  
Определение активного пункта по URL  
Использование явных и именованных URL в пунктах меню  
Загрузка всех данных за один SQL-запрос  
Редактирование через стандартную админку Django  

## Установка
Склонируйте репозиторий  
Перейдите в папку проекта:  
cd tree_menu  
Установите зависимости:  
pip install -r requirements.txt  
Выполните и применити миграции:  
python manage.py makemigrations  
python manage.py migrate  
Создайте суперпользователя:  
python manage.py createsuperuser  
Запустите сервер разработки:  
python manage.py runserver  

## Использование
Зайдите в Django Admin и создайте элементы меню через раздел "Элементы меню".

На нужной странице подключите шаблонный тег:

{% load menu_tags %}  
{% draw_menu 'main_menu' %}  
(где 'main_menu' — это название меню, заданное в БД)
