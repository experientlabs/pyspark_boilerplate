

<img src="../resources/images/to_do.png" alt="to_do" style="height:419px; width:1072px; margin: -40px 50px -60px 0px; overflow: hidden;"/>


WIP:
Adding Tests, Run tests using command line and generate coverage report
Generate documentation
Complete CI tests.  

# Why setup.cfg? 
If you are using a setup.cfg file for your project configuration, you can add the flake8 section with the max-line-length option:
Setup.cfg supports various settings.



# High level TODO
- Add Architecture Diagram.
- Refactoring to make it compatible
- Feature to turn off logging
- Feature for Dry Run
- Unit Test
- Integration Test
- Versioning
- Documentation
- Command line parameters for make file (Make)
- Add CICD so that CI test can be executed by commenting specific string in the gihub comment box.
- [Decorators](https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a)
- Monads
- [Use Dataclass](https://zetcode.com/python/dataclass/)
- Zepplin
- Bridging Spark SQL with JDBC


# Low leve TODO
1. package resources API to get rid of `project_root_dir.py`.
2. path lib to avoid path conflict between windows and linux. 


### Notes:
What else to do 
1. CI-CD
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
But the goal is to update it back to 3.5 or the latest version, Alsong with docker image.