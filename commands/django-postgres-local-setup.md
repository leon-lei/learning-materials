# Commands to set up Postgres for local
Referencing:
https://medium.com/agatha-codes/painless-postgresql-django-d4f03364989

## In the CMD Terminal
```
psql
```

## Create a user first
```
CREATE USER <name> WITH PASSWORD <password>;

# Example
CREATE USER carlton WITH PASSWORD 'banks'; 
```

## Create a database and give the new user access
```
CREATE DATABASE databasename OWNER namehere;

# Example 
CREATE DATABASE belaire WITH OWNER carlton;
```

## Django settings file
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'belaire',
        'USER': 'carlton',
        'PASSWORD': 'banks',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```