

<img src="../resources/images/to_do.png" alt="to_do" style="height:419px; width:1072px; margin: -40px 50px -60px 0px; overflow: hidden;"/>

# TODO 
https://www.youtube.com/watch?v=OyQAjXeY4cU

# 1. Code
This section is work in progress, and functional with basic features.
   Optimize image size, takes time to load
   Add more innovative use cases
   More on CICD. 

# 2. Spark Environment in Docker
This section is also work in progress and functional with basic features. 

# 3. Airflow (Scheduler)
To be started

# Why setup.cfg? 
If you are using a setup.cfg file for your project configuration, you can add the flake8 section with the max-line-length option:
Setup.cfg supports various settings.



# High level TODO
- More on CICD
- Add Architecture Diagram.
- Integration Test
- Versioning
- Documentation
- Command line parameters for make file (Make)
- [Decorators](https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a)
- Monads
- [Use Dataclass](https://zetcode.com/python/dataclass/)
- Zepplin
- Bridging Spark SQL with JDBC


# Future Path: 
1. package resources API to get rid of `project_root_dir.py`.
2. path lib to avoid path conflict between windows and linux. 
3. Meaningful unit test and Integration tests. 


### Notes:
What else to do
2. Secrets Manager/ Hashicorp Vault
3. Spark Streaming
4. Spark ML
   - pack size optimization.
   - mark-up, mark-down.
   - floor price prediction.
5. Graph Processing
6. Python Shiny Graph
7. Airflow DAG
8. Packaging and Distribution

Using function as a decorator:
- Using @property decorator
- Implement @abstractmethod
- Implement @staticmethod
- Implement ABC
- Use @dataclass(frozen = true)


To avoid the compatibility issue with docker image, I have used pyspark==3.2.4 
But the goal is to update it back to 3.5 or the latest version, Also updated the spark version
in docker image.