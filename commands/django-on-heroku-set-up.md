# Instructions on setting up an existing Django project in Heroku
# Assumes the setting file is using environment variables for sensitive variables

1. Set up a virtual environment with Pipfile and Pipfile.lock
    1. *pipenv install*
    2. *pipenv shell*

------------------------------------------------
2. Initialize a git repository
    1. *git init*
    2. *git add .*
    3. *git commit -m "Messsage here"*

------------------------------------------------
3. Create a heroku project 
    1. *python manage.py collectstatic*
    2. *heroku create projectname-foobar*

------------------------------------------------
4. Configure variables in heroku project through UI
    1. ALLOWED_HOSTS
    2. DJANGO_SECRET_KEY
    3. DJANGO_SETTINGS_MODULE
    4. *heroku config* to check if set properly

------------------------------------------------
5. Provision Heroku Postgres if not already provisioned
    1. *heroku addons* to check
    2. If not already provisioned:
        1. heroku addons:create heroku-postgresql:<PLAN_NAME>
        2. *heroku addons:create heroku-postgresql:hobby-dev*

------------------------------------------------
6. Push local project into heroku
    1. *git push heroku master*
    2. *heroku run python manage.py makemigrations*
    3. *heroku run python manage.py migrate*
    4. *heroku run python manage.py createsuperuser*
    5. *heroku open*
