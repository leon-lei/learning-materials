# Instructions on setting up an existing Django project in Heroku
Assumes the setting file is using environment variables for sensitive variables

## 1. Set up a virtual environment with Pipfile and Pipfile.lock
```
pipenv install
pipenv shell
```

## 2. Initialize a git repository
```
git init
git add .
git commit -m "Messsage here"
```

## 3. Create a heroku project 
```
python manage.py collectstatic
heroku create projectname-foobar
```

## 4. Configure variables in heroku project through UI
    1. ALLOWED_HOSTS
    2. DJANGO_SECRET_KEY
    3. DJANGO_SETTINGS_MODULE
    4. *heroku config* to check if set properly

## 5. Provision Heroku Postgres if not already provisioned
```
# check to see if already provisioned
heroku addons

# if not provisioned
# heroku addons:create heroku-postgresql:<PLAN_NAME>
heroku addons:create heroku-postgresql:hobby-dev
```

## 6. Push local project into heroku
```
git push heroku master
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku open
```