import os
import urllib

import pytest

from etl.data_jobs.air_asia_data_job import AirADataJob


class TestAirADataJob:

    #  Read the nested json file from url and process it
    def test_read_nested_json(self):
        job = AirADataJob("air_asia_data_job")
        job.run()
        # Assert that the superman.json file is stored at the specified landing path
        assert os.path.exists(job.superman_landing_path + "/superman.json")
        # Assert that the superman_final.json file is created at the specified target path
        assert os.path.exists(job.superman_target_path + "/superman_final.json")

    #  Read data from random user API and process it
    def test_read_random_user_api(self):
        job = AirADataJob("air_asia_data_job")
        job.run()
        # Assert that the random user data is dumped at the specified landing path
        assert os.path.exists(job.random_user_landing_path)
        # Assert that the processed data is placed at the specified target path
        assert os.path.exists(job.random_user_target_path + "/assessment_2_total_count")

    #  Flatten json data
    def test_flatten_json(self):
        job = AirADataJob("air_asis_data_job")
        json_list = job.flatten_json(job.superman_landing_path)
        # Assert that the returned json list is not empty
        assert len(json_list) > 0

    #  Invalid url for json file
    def test_invalid_json_url(self):
        job = AirADataJob("air_asia_data_job")
        # Set an invalid url for the json file
        job.json_url = "https://invalid_url"
        with pytest.raises(urllib.error.URLError):
            job.run()

    #  Invalid url for random user API
    def test_invalid_random_user_api_url(self):
        job = AirADataJob("air_asia_data_job")
        # Set an invalid url for the random user API
        job.url = "https://invalid_url"
        with pytest.raises(urllib.error.URLError):
            job.run()

    #  Invalid path for landing and target directories
    def test_invalid_paths(self):
        job = AirADataJob("air_asia_data_job")
        # Set invalid paths for landing and target directories
        job.superman_landing_path = "/invalid_path"
        job.superman_target_path = "/invalid_path"
        job.random_user_landing_path = "/invalid_path"
        job.random_user_target_path = "/invalid_path"
        with pytest.raises(Exception):
            job.run()
