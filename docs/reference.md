# References
1. Image Source: https://datascientest.com/en/pyspark-the-python-library
2. Shell Script: https://github.com/diogocavilha/respect-shell
3. Python Versioning: https://towardsdatascience.com/setup-version-increment-and-automated-release-process-591d87ea1221
    - https://github.com/mbalatsko/release-version-incremen
4. Makefile vs ShellScript: https://unix.stackexchange.com/questions/496793/script-or-makefile-to-automate-new-user-creation/497601#497601
5. Make Error, make: target is up to date - https://nono.ma/make-target-is-up-to-date
6. Other links: 
   - https://stackoverflow.com/questions/54797832/why-does-spark-submit-fail-with-error-executing-jupyter-command
   - https://janetvn.medium.com/how-to-add-multiple-python-custom-modules-to-spark-job-6a8b943cdbbc
   - https://stackoverflow.com/questions/46429962/how-to-redirect-entire-output-of-spark-submit-to-a-file
   - https://stackoverflow.com/questions/67267683/do-we-need-if-name-main-unittest-main-in-every-unit-tests-file
   - https://stackoverflow.com/questions/25436312/gitignore-not-working
   - https://stackoverflow.com/questions/38776517/how-to-discard-local-changes-and-pull-latest-from-github-repository
   - How to enforce schema on Pyspark Job?
     - https://github.com/MrPowers/quinn/blob/main/quinn/dataframe_validator.py
     - https://stackoverflow.com/questions/63040466/enforcing-schema-for-pyspark-job

   - How to write a single csv file without a Folder?
     - https://stackoverflow.com/questions/43661660/spark-how-to-write-a-single-csv-file-without-folder/60442604#60442604
7. Reference projects
   - https://github.com/mehd-io/pyspark-boilerplate-mehdio/blob/master/docker/script/package_zip.sh


# Link of Data
List of websites that provide Real time data.
1. https://data.nasa.gov
2. flight status api
3. https://developer.accuveather.com
4. Twitter APIs
5. News APIs

List of Streaming Data for Spark Streaming. 
1. To be added
2. Music Reommendation Dataset 
   - http://ocelma.net/MusicRecommendationDataset/lastfm-1K.html

# Reference Commands: 

1. Python clean and build command
python3 setup.py clean
python3 setup.py sdist --format=zip


2. Creating requirements.txt file

```commandline
pip3 freeze > requirements.txt  #Python3
```

3. Make File Analysis using ChatGPT

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
- The -m3 flag sets the multi-line import style to "vertical hanging indent".
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


### Notes from readme file:

#### Note-1
I have tried to add more than one way of doing same thing to demonstrate different ways of performing a similar task. 
For example in order to fetch configs and Constants, 
I am using following approach here:
1. Config file with extension .cfg/ini read and parsed by configparser in config_utils.py 
2. Constants.py containing dictionary --  This has been replaced by Enum 
3. Constants.py containing Enum class

#### Note-2
In order to avoid relative path issue, I have tried `package resources api` from setuptools. 
later on this was changed with a python file in root directory named `project_root_dir.py`
The goal is to switch back to package resources api after the project is stable.