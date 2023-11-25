# Pyspark Boilerplate

<img src="pyspark_boilerplate.png" alt="drawing" style="height:419px; width:1072px;"/>

## Preface: 
This is a sample pyspark project designed to work as a boilerplate application. This application is written by following 
object oriented programming and various Design Principles like Abstract Base Class (ABC), Factory Design, Singleton Design Patterns etc. 

The goal behind developing this project is to provide a real exposure to Pyspark and python coding as a production 
environment. And make this boilerplate as production ready as possible using my limited knowledge and experience.

I have tried to add more than one way of doing same thing to demonstrate different ways of performing a similar task. 
For example in order to fetch configs and Constants, 
I am using following approach here:
1. Config file with extension .cfg/ini read and parsed by configparser in config_utils.py 
2. Constants.py containing dictionary --  This has been replaced by Enum 
3. Constants.py containing Enum class


In terms of coverage of spark topics, the goal is to cover all of the High level spark features mentioned here
 - Spark SQL
 - Spark Streaming
 - MLlib
 - GraphX

<img src="img.png" alt="drawing" style="width:500px;"/>


### Setup: Running it locally
In order to use this boilerplate follow the instructions mentioned below: 

1. Set up the `PYTHONPATH`
    ```commandline
    rootfolder="$(pwd)"
    export PYTHONPATH=$PYTHONPATH:$rootfolder
    ```

2. Run this app from command line: Currently there are total 3 pipelines as part of this project.
In order to test the pipeline you can run any or all three jobs locally by running below command. 
All three pipelines should run successfully

    ```
   python3 etl/etl_job.py --job_name air_asia_data_job
   python3 src/app/app.py --job-name happiness_index_job
   python3 src/app/app.py --job-name bmi_data_job
    ```





- In order to avoid relative path issue, I have tried package resources api from setuptools. 
later on this was changed with a python file in root directory named `project_root_dir.py`
The goal is to switch back to package resources api after the project is stable.



```	
spark-submit \
	--jars jars/any-jar_0.1-0.1.1.jar \
	--py-files datajob.zip \
	src/app/app.py \
	--job-name air_asia_data_job
```

While running spark-submit in spark jupyter docker container. I was getting error:
Jupyter command `file/path` not found
Below stackoverflow article answers this problem. That has to do with  PYSPARK_DRIVER_PYTHON=jupyter
Which should be set to PYSPARK_DRIVER_PYTHON=python. 

export PYSPARK_DRIVER_PYTHON=python
export PYTHONPATH=PYTHONPATH:spark_etl/





### Notes:

What else to do 
1. CI-CD
2. Secrets Manager/ Hashicorp Vault
3. Spark Streaming
4. Spark ML
5. Graph Processing
6. Python Shiny Graph
7. Airflow DAG
8. Packaging and Distribution


List of websites that provide Real time data.
1. https://data.nasa.gov
2. flight status api
3. https://developer.accuveather.com
4. Twitter APIs
5. News APIs

List of Streaming Data for Spark Streaming. 


How to enforce schema on Pyspark Job?
https://github.com/MrPowers/quinn/blob/main/quinn/dataframe_validator.py
https://stackoverflow.com/questions/63040466/enforcing-schema-for-pyspark-job


How to write a single csv file without a Folder?
https://stackoverflow.com/questions/43661660/spark-how-to-write-a-single-csv-file-without-folder/60442604#60442604


http://ocelma.net/MusicRecommendationDataset/lastfm-1K.html

Why config directory should be out of src?


https://stackoverflow.com/questions/67267683/do-we-need-if-name-main-unittest-main-in-every-unit-tests-file


https://github.com/orgs/community/discussions/25389


What is decorator design pattern? Provide at least one example of Decorator Design Pattern in this code?


https://github.com/mehd-io/pyspark-boilerplate-mehdio/blob/master/docker/script/package_zip.sh



## pytest -vvv -rf -q --cov --cov-report term $(PY_MODULES) $(PYTESTFLAGS)
The pytest command runs the pytest testing framework on the specified modules.
The -vvv flag sets the verbosity level to "very very verbose", which means that pytest will print a lot of information about each test.
The -rf flag shows "only failed tests and any important information", suppressing the output for passing tests.
The -q flag suppresses extra information when running tests.
The --cov flag enables code coverage measurement with pytest-cov.
The --cov-report term flag specifies that coverage statistics should be printed to the terminal in a simple format.
The $(PY_MODULES) variable should contain a space-separated list of Python module file paths to be tested by pytest.
The $(PYTESTFLAGS) variable can contain additional command-line flags and options to be passed to pytest.

So when you run make test-unit, it will execute the pytest command with the specified options, running the unit tests and measuring code coverage for the specified modules.

https://stackoverflow.com/questions/25436312/gitignore-not-working

https://stackoverflow.com/questions/38776517/how-to-discard-local-changes-and-pull-latest-from-github-repository


Using function as a decorator:
Using @property decorator
Implement @abstractmethod
implement @staticmethod

Implement ABC
Use @dataclass(frozen = true)


