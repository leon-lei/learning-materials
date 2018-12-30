# Pytest Practice

Referencing Brian Okken's Python Testing with pytest

## Running only one test
```
pytest -v tasks/test_four.py::test_asdict
```

## Options
```
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