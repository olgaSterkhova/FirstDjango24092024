# django 23092024
# Инструкция по развертыванию проекта
# Создать виртуальное окружение:
# python3 -m venv django_venv
# Aктивировать виртуальное окружение:
# source django_venv/bin/activate
# Установить нужные пакеты:
# python -m pip install -r requirements.txt
# Применить все миграция для создания таблиц в БД python manage migrate
# Запустить сервер:
# python manage.py runserver
# Запуск ipython в контексте приложений проекта django
# python manage.py shell_plus --ipython
# Выгрузка и загрузка данных
# Выгрузить данные из БД
# python manage.py dumpdata MainApp --indent 4 > MainApp/fixtures/save_all.json
# Загрузить данные в БД
# python manage.py loaddata MainApp/fixtures/save_all.json