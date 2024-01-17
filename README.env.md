# todoapp_env
paso 1: workon todoapp_venv
paso 2: pip install Django
paso 3: django-admin startproject todoapp
paso 4: cd todoapp
paso 5: python manage.py startapp core
paso 6: ALTER USER todoapp_user WITH PASSWORD '12345678a';
paso 7: python manage.py makemigrations
paso 8: python manage.py migrate
paso 9: python manage.prunserver 8081
paso 10: python manage.py createsuperuser
paso 11: echo "# todoapp_env" >> README.env.md
