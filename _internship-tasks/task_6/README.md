# TASK 6
Create a delta/csv spark table and build a data transformation pipeline with at least 3 aggregations and filtering

## Content
* `impressions.csv`, dataset in AdTech domain from Task 1 (train.csv)
* `task_6.py`, ETL pipeline which reads, transforms and loads data in Spark/Delta format
* `task_6.ipynb`, the same ETL job, but in jupiter notebook
* `unit_tests.py`, unit tests
* `data_quality.py`, data quality tests
* `requirements.txt`, file with prod dependencies
* `requirements-dev.txt`, file with dev dependencies
* `Makefile`, make file to run tests


## How to run tests
To run unit tests and data quality tests, you need to execute the command in the terminal
```
  make init test
```

## how to execute ETL job
To run the ETL pipeline, you need to execute the command in the terminal
```
  make init
  python3 task_6.py
```