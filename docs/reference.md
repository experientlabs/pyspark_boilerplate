python3 setup.py sdist --format=zip



How to manage version of a Python Project?
https://towardsdatascience.com/setup-version-increment-and-automated-release-process-591d87ea1221


# Versioning
https://github.com/mbalatsko/release-version-incremen
https://towardsdatascience.com/setup-version-increment-and-automated-release-process-591d87ea1221

# Shell Script
https://github.com/koalaman/shellcheck/wiki/SC2164
https://github.com/diogocavilha/respect-shell


# Make File

```pytest -vvv -rf -q --cov --cov-report term $(PY_MODULES) $(PYTESTFLAGS)```

The pytest command runs the pytest testing framework on the specified modules.
The -vvv flag sets the verbosity level to "very very verbose", which means that pytest will print a lot of information about each test.
The -rf flag shows "only failed tests and any important information", suppressing the output for passing tests.
The -q flag suppresses extra information when running tests.
The --cov flag enables code coverage measurement with pytest-cov.
The --cov-report term flag specifies that coverage statistics should be printed to the terminal in a simple format.
The $(PY_MODULES) variable should contain a space-separated list of Python module file paths to be tested by pytest.
The $(PYTESTFLAGS) variable can contain additional command-line flags and options to be passed to pytest.

So when you run make test-unit, it will execute the pytest command with the specified options, running the unit tests and measuring code coverage for the specified modules.


```
test-mypy:  # typing check
	mypy $(PY_MODULES)
```
Here's how it works:

The target is test-mypy.
The command to run is mypy $(PY_MODULES).
The mypy command runs the mypy tool on the specified modules.
The $(PY_MODULES) variable should contain a space-separated list of Python module file paths to be checked by mypy.
So when you run make test-mypy, it will execute the mypy command on the specified modules, checking for type errors and inconsistencies in your Python code.


```test-isort:
	isort -l80 -m3 -c --tc $(PY_MODULES)
```

Here's how it works:

- The target is test-isort.
- The command to run is isort -l80 -m3 -c --tc $(PY_MODULES).
- The isort command checks the import order of the specified modules.
- The -l80 flag sets the line length to 80 characters.
- The -m3 flag sets the multi-line import style to "vertial hanging indent".
- The -c flag makes isort only check the import order and not apply any changes.
- The --tc flag prints a unified diff of the changes that would be made by isort.
- The $(PY_MODULES) variable should contain a space-separated list of Python module file paths to be checked by isort.
So when you run make test-isort, it will execute the isort command on the specified modules, checking their import order against the specified style rules and printing a diff of any changes that would be made.



```
coverage:
	coverage run --source=. -m unittest discover tests/
	coverage report --fail-under=80
	coverage html

```
The target is named coverage.
The command to run is coverage run --source=. -m unittest discover tests/.
The coverage command runs your unit tests with coverage measurement and produces a coverage report in a .coverage file.
The --source=. option tells coverage to measure coverage for all files in the current directory.
The -m flag specifies that the unittest module should be run as a module.
The discover command finds and runs all the unit tests in the tests/ directory.
The second command coverage report --fail-under=80 generates a coverage report in the terminal with a minimum coverage threshold of 80%.
The third command coverage html generates a HTML report from the .coverage file.
This assumes that you have installed the coverage package and your unit tests are located in a tests/ subdirectory of your project.

You can add this target to your existing Makefile by simply appending these lines to the end of the file. Then you can run make coverage to run your unit tests with coverage measurement and produce coverage reports in both the terminal and a HTML file. The HTML report will be saved in a htmlcov/ directory.


## Make is Up to Date Error:
https://nono.ma/make-target-is-up-to-date





Implement Logging Decorator Function as given below
https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a


Implement Timing Decorator Function to get runtime 
https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a

Use Dataclass 
https://zetcode.com/python/dataclass/

Feature to turn off logging


logs directory, should it be pushed as part of deployment?
Configurable logging


#### What are advantages and disadvantages of using zip as python application?


### How to avoid path conflict in python? like when we give relative path of config file, or logs directory, This fails when environment changes. 

By using Absolute Path:
```python
import os

# get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# use the absolute path to the config file
config_file_path = os.path.join(script_dir, 'config.ini')

# use the absolute path to the log directory
log_dir_path = os.path.join(script_dir, 'logs')

```

Or by using Environment Variable

```python
import os

# get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# use the absolute path to the config file
config_file_path = os.path.join(script_dir, 'config.ini')

# use the absolute path to the log directory
log_dir_path = os.path.join(script_dir, 'logs')

```


How to redirect entire output of spark-submit to a file
https://stackoverflow.com/questions/46429962/how-to-redirect-entire-output-of-spark-submit-to-a-file



# ToDo:
Add CICD so that CI test can be executed by commenting specific string in the gihub comment box. 