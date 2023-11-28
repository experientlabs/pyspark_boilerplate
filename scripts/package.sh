#!/bin/bash
source scripts/respect.sh
# Package pyspark etl application and its python dependencies into a `pyspark_etl_job.zip` folder

mkdir to_upload
pip3 freeze > requirements.txt
pip3 -q install -r requirements.txt -t to_upload
#rm -r requirements.txt
cp -r {setup.py,tasks.py,project_root_dir.py,etl,README.md,VERSION,MANIFEST.in} to_upload
cd to_upload || exit

version=$(echo `python3 setup.py --version` | sed s/_/-/g)

echo "+++++++++++++++++++++++"
echo "$version"
echo "+++++++++++++++++++++++"
python3 setup.py sdist --format=zip
echo "+++++++++++++++++++++++"
echo "unzipping the sdist/spark-spark_etl-version.zip"
echo "+++++++++++++++++++++++"
unzip -q "dist/spark_etl-$version.zip"
cd "spark_etl-$version" || exit
# Small hack so that main package (etl) can be added to python path
touch __init__.py
mkdir ../../target
zip -q -r "../../target/spark_etl-$version.zip" *
cd ../../
pwd
rm -r to_upload


