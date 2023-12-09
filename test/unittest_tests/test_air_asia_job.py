import os
import unittest

from etl.config import config_utils
from etl.data_jobs.air_asia_data_job import AirADataJob
from etl.utils import spark_utils
from test.utils_functions import update_unittest_path


class TestAirADataJob(unittest.TestCase):

    #  Read the nested json file from url and process it
    def test_read_nested_json(self):
        job = AirADataJob("air_asia_data_job")
        job.run()
        # Assert that the superman.json file is stored at the landing path
        self.assertTrue(os.path.exists(job.superman_landing_path + "/superman.json"))
        # Assert that the superman_final.json file is created at the target path
        self.assertTrue(os.path.exists(job.superman_target_path + "/superman_final.json"))

    #  Read data from random user API and process it
    def test_read_random_user_api(self):
        job = AirADataJob("air_asia_data_job")
        job.run()
        # Assert that the random user data is dumped at the landing path
        self.assertTrue(os.path.exists(job.random_user_landing_path))
        # Assert that the processed data is placed at the target path
        self.assertTrue(os.path.exists(job.random_user_target_path))

    #  Flatten json data
    def test_flatten_json(self):
        """
        In real project there should be test data setup, here we are using real data for test purpose
        As data volume is very small.
        """
        job = AirADataJob("air_asia_data_job")
        test_path = os.path.abspath(job.superman_landing_path).replace("test/unittest_tests", "")
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
