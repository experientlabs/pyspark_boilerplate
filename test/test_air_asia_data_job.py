# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     15/01/23 11:55 am
# File:             test_air_asia_data_job.py
# -----------------------------------------------------------------------
import os
import unittest
from unittest.mock import Mock, patch

from etl.data_jobs.air_asia_data_job import AirADataJob
from etl.utils import spark_utils
from etl.config import config_utils
from test.utils_functions import update_test_path


class TestAirA(unittest.TestCase):
    """
    TODO: Add test for all functions. Currently it is skeleton only
    """

    utils = spark_utils.SparkUtils()
    spark = utils.get_spark_session("air_asia_data_job")

    config_path = "../etl/config/pipeline.cfg"
    configutil = config_utils.ConfigUtil(config_path)
    configutil.get_config("IO_CONFIGS", "INPUT_DATA_PATH")

    # @staticmethod
    # def update_test_path(path: str) -> str:
    #     return os.path.abspath(path).replace("test/", "")

    def test_read_nested_json(self):
        job = AirADataJob("air_asia_data_job")
        # Assert that the superman.json file is stored at the landing path
        # This is similar to testing the target and source database connection in real project stetting.
        landing_path = update_test_path(job.superman_landing_path)
        self.assertTrue(os.path.exists(landing_path + "/superman.json"))
        # Assert that the superman_final.json file is created at the target path
        target_path = update_test_path(job.superman_target_path)
        self.assertTrue(os.path.exists(target_path + "/superman_final.json"))

        #  Read data from random user API and process it

    def test_read_random_user_api(self):
        job = AirADataJob("air_asia_data_job")
        # job.run()
        # Assert that the random user data is dumped at the landing path
        ru_landing_path = self.update_test_path(job.random_user_landing_path)
        self.assertTrue(ru_landing_path)
        # Assert that the processed data is placed at the target path
        ru_target_path = self.update_test_path(job.random_user_target_path)
        self.assertTrue(ru_target_path)

        #  Flatten json data

    def test_flatten_json(self):
        """
        In real project there should be test data setup, here we are using real data for test purpose
        As data volume is very small.
        """
        job = AirADataJob("air_asia_data_job")
        test_path = os.path.abspath(job.superman_landing_path).replace("test/", "")
        json_list = job.flatten_json(test_path)
        # Assert that the returned json list is not empty
        self.assertTrue(len(json_list) > 0)

        #  Invalid url for json file

    def test_invalid_json_url(self):
        job = AirADataJob("air_asia_data_job")
        # Set an invalid url for the json file
        job.json_url = "https://invalid_url"
        # Assert that an exception is raised when reading the json file
        with self.assertRaises(Exception):
            job.run()

        #  Invalid url for random user API

    def test_invalid_api_url(self):
        job = AirADataJob("air_asia_data_job")
        # Set an invalid url for the random user API
        job.json_url = "https://invalid_url"
        job.url = "https://invalid_url"
        # Assert that an exception is raised when reading the API data
        with self.assertRaises(Exception):
            job.run()

        #  Invalid path for landing and target directories

    def test_invalid_directory_path(self):
        job = AirADataJob("air_asia_data_job")
        # Set an invalid path for the landing and target directories
        job.superman_landing_path = "/invalid_path"
        job.superman_target_path = "/invalid_path"
        # Assert that an exception is raised when reading the json file and processing it
        with self.assertRaises(Exception):
            job.run()

    def test_aa_data_job(self):
        pass
        # spark = spark_utils.SparkUtils().get_spark_session("aa_data_job")
        # aa_helper: AirAHelper = AirAHelper(spark)
        # air_data_job = AirADataJob()
        # print(air_data_job.url)
        # print(air_data_job.json_url)
        # print(air_data_job.superman_landing_path)
        # aa_helper.read_json_from_web(air_data_job.json_url, air_data_job.superman_landing_path)
        # json_list = air_data_job.flatten_json(air_data_job.superman_landing_path)
        # print(air_data_job.process_json(json_list, air_data_job.superman_target_path))
        # aa_helper.ingest_api_data(air_data_job.url, air_data_job.random_user_target_path)

    def test_calculate_bmi(self):
        """
        TODO: Complete this test test_calculate_bmi
        :return:
        """
        print(f"this is a skeleton Test")
        pass

    def test_get_bmi_category(self):
        """
        TODO: Complete this test test_get_bmi_category
        :return:
        """
        pass

    def test_get_record_count(self):
        """
        TODO: Complete this test test_get_record_count
        :return:
        """
        pass

    def test_run(self):
        """
        TODO: Complete this test test_run
        :return:
        """
        pass
