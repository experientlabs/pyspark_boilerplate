import os
import re
from setuptools import find_packages, setup
import pathlib
import tasks
from project_root_dir import project_root_dir

here = pathlib.Path(__file__).parent.resolve()

with open(f"{here}/README.md", "r") as readme_file:
    long_description = readme_file.read()

pre_release_placeholder = 'SNAPSHOT'
version_filepath = os.path.join(project_root_dir, 'etl/VERSION')
version_pattern = re.compile(fr'^\d+.\d+.\d+(-{pre_release_placeholder})?$')


setup(
    name="spark_etl",
    version=tasks.get_version(),
    author="Sanjeet Shukla",
    author_email="sanjeet.shukla089@gmail.com",
    packages=find_packages(exclude=["test"]),
    package_data={
        "": ["*.cfg", "*.ini", "*.py", "tasks.py", "VERSION", "project_root_dir.py"]
    },
    include_package_data=True,
    description="A pyspark boilerplate with Object Oriented Design",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/experientlabs/pyspark_boilerplate",
    license='CC BY-NC 4.0',
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "app=et.etl_job.app:app",
        ],
    },

    test_suite='tests',
    project_urls={
        "Bug Reports": "https://github.com/experientlabs/pyspark_boilerplate/issues",
        "Funding": "https://donate.pypi.org",
        "Say Thanks!": "https://saythanks.io/my_project",
        "Source": "https://github.com/experientlabs/pyspark_boilerplate"
    }
)