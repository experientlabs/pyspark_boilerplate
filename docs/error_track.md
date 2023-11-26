1. Error: Py4JException: `Constructor org.apache.spark.sql.SparkSession([class org.apache.spark.SparkContext, class java.util.HashMap]) does not exist`
   - The reason for this error was due to different version of spark in code and in docker image.
   - In docker container it was spark 3.2.4, but in code it was pyspark version 3.5.0
   - To get rid of this error, I changed the pyspark version to 3.2.4 in `requirements.txt`
2. Error: RuntimeError: Python in worker has different version 3.7 than that in driver 3.10, PySpark cannot run with different minor versions. 
Please check environment variables `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` are correctly set.
