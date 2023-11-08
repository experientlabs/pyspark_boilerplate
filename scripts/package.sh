#!/bin/bash
source scripts/respect.sh
# Package pyspark etl application and its python dependencies into a `pyspark_etl_job.zip` folder

version=$(echo `python3 setup.py --version` | sed s/_/-/g)
echo "$version"
python3 setup.py sdist --format=zip
pwd
unzip -q "dist/spark_etl-$version.zip"
cd "spark_etl-$version" || exit
# Small hack so that main package (src) can be added to python path
touch __init__.py
zip -q -r "../../target/spark_etl-$version.zip" *
cd ../../
pwd
