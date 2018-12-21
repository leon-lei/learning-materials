# Pipenv Command Line

## Installing specific versions of Python
```
pipenv --python 3
pipenv --python 3.6
```

## Install specific versions of Packages
```
pipenv install django==2.0.7
```

## Install packages for development
```
pipenv install pytest --dev

# Installs all pkgs listed under [dev-packages]
pipenv install --dev
```


## See path of virtual environment
```
pipenv --venv
```

## Graph of packages and dependencies
```
pipenv graph
```

## Activate virtual environment in subshell
```
pipenv shell
```

## Run a program with virtual environment
```
pipenv run foobar.py
```

## Remove virtual environment
```
pipenv --rm
```

## Create new virtual environment from Pipfile and Pipfile.lock
Note this will destroy existing virtual environment in the directory
```
pipenv install
```