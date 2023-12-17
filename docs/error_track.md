1. Error: Py4JException: `Constructor org.apache.spark.sql.SparkSession([class org.apache.spark.SparkContext, class java.util.HashMap]) does not exist`
   - The reason for this error was due to different version of spark in code and in docker image.
   - In docker container it was spark 3.2.4, but in code it was pyspark version 3.5.0
   - To get rid of this error, I changed the pyspark version to 3.2.4 in `requirements.txt`
2. Error: RuntimeError: Python in worker has different version 3.7 than that in driver 3.10, PySpark cannot run with different minor versions. 
Please check environment variables `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` are correctly set. 
   - export PYSPARK_DRIVER_PYTHON=/usr/bin/python3 
   - export PYSPARK_PYTHON=/usr/bin/python3

3. PATH error:Error in main driver function Path does not exist: Issue due to relative path for source and target data file, 
based on which directory I trigger the job from. the path will get changed. resulting in error message. 
   - Plan is to use `project_root_directory` for paths.


4. Github Actions ci test failure
   - Error in github actions. 
```======================================================================
ERROR: test_flatten_json (test_air_asia_data_job.TestAirA)
In real project there should be test data setup, here we are using real data for test purpose
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/pyspark_boilerplate/pyspark_boilerplate/test/test_air_asia_data_job.py", line 59, in test_flatten_json
    json_list = job.flatten_json(test_path)
  File "/home/runner/work/pyspark_boilerplate/pyspark_boilerplate/etl/data_jobs/air_asia_data_job.py", line 84, in flatten_json
    with open(path + "/superman.json", encoding="utf-8") as f:
FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/pyspark_boilerplate/pyspark_boilerplate/resources/data/source_data/aa_data/superman.json'

======================================================================
FAIL: test_read_nested_json (test_air_asia_data_job.TestAirA)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/pyspark_boilerplate/pyspark_boilerplate/test/test_air_asia_data_job.py", line 33, in test_read_nested_json
    self.assertTrue(os.path.exists(landing_path + "/superman.json"))
AssertionError: False is not true

======================================================================
FAIL: test_config_utils (test_config_utils.TestConfigUtils)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/pyspark_boilerplate/pyspark_boilerplate/test/test_config_utils.py", line 28, in test_config_utils
    assert superman_landing_path == "resources/data/source_data/aa_data"
AssertionError
```