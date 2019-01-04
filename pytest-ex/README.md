# Pytest Practice

Referencing Brian Okken's Python Testing with pytest

## Install tasks module within pipenv
```
# -e (editable) allows modification to source code while tasks is installed
pipenv install -e ./tasks_proj/
```

## Running only one test
```
pytest -v tasks/test_four.py::test_asdict
```

## Running subset of tests
```
# double colon to specify and get more granular
$ pytest -v tests/func/test_add.py::test_add_returns_valid_id

# test a single method of a test class
$ pytest -v tests/func/test_api_exceptions.py::TestUpdate::test_bad_id
```

## Parameterizing tests
```
# see test_add_variety.py

@pytest.mark.parametrize(argnames, argvalues)

@pytest.mark.parametrize('tasks', [Task(1), Task(2), Task(3)])

@pytest.mark.parametrize('summary, owner, done', [('sleep', None, False), ('code', 'Leon', True)])
```

## Options
```
# Chars (show extra test summary info)
# Example below show summary info for skip tests
$ pytest -rs

# Collect only
$ pytest --collect-only

# Duration
# Reports the slowest N number of test/setups/teardowns after the tests run
$ pytest --durations=3

# Expressions
$ pytest -k 'asdict or defaults'

# Local variables
$ pytest -l

# Markers
$ pytest -m run_these_please

# Tracebacks
$ pytest --tb=no
$ pytest --tb=line (prints line of failure)

# Verbose
$ pytest -v

# Quiet
# Use in conjunction with traceback for terse outputs
$ pytest -q --tb=line


###################### Failures ######################
# exit at first failure
$ pytest -x

# last failed
$ pytest --lf

# failed first (runs rest of test that passed last time after failed test)
$ pytest --ff

# max fails
$ pytest --maxfail=2
######################################################
```

## See all available fixtures or markers
```
$ pytest --fixtures

$ pytest --markers
```

## Fixtures
```
# see which fixtures ran with the test
$ pytest --setup-show test_add.py -k valid_id

# see where fixtures are defined
$ pytest --fixtures tests/func/test_add.py
```

## Scopes
```
@pytest.fixture(scope='function')

@pytest.fixture(scope='class')

@pytest.fixture(scope='module')

@pytest.fixture(scope='session')
```

## Cached
```
$ pytest --cache-show

$ pytest --cache-clear
```