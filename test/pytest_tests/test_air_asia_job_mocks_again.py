import pytest
from pytest_mock import mocker, module_mocker, class_mocker, package_mocker
from etl.data_jobs.air_asia_data_job import AirADataJob


class TestAirADataJob:

    #  Reads the nested json file from url and processes it
    def test_read_nested_json_from_url(self, mocker):
        # Write test to setup test data.
        # Mock the necessary dependencies
        mocker.patch('etl.data_jobs.air_asia_data_job.urllib.request.urlopen')
        mocker.patch('etl.data_jobs.air_asia_data_job.open')
        mocker.patch('etl.data_jobs.air_asia_data_job.os.makedirs')
        mocker.patch('etl.data_jobs.air_asia_data_job.AirADataJob.logger')

        # Initialize the class
        job = AirADataJob("air_asia_data_job")

        # Invoke the method being tested
        job.aa_helper.read_json_from_web.return_value = None
        job.read_json_from_web("url", "landing_path")

        # Assert the expected behavior
        job.aa_helper.read_json_from_web.assert_called_once_with("url", "landing_path")

    #  Reads data from random user API and processes it
    def test_read_api_data(self, mocker):
        # Write test to setup test data.
        # Mock the necessary dependencies
        mocker.patch('etl.data_jobs.air_asia_data_job.urllib.request.urlopen')
        mocker.patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.get_spark_session')
        mocker.patch('etl.data_jobs.air_asia_data_job.AirADataJob.logger')

        # Initialize the class
        job = AirADataJob("air_asia_data_job")

        # Invoke the method being tested
        job.aa_helper.ingest_api_data.return_value = None
        job.ingest_api_data("url", "landing_path")

        # Assert the expected behavior
        job.aa_helper.ingest_api_data.assert_called_once_with("url", "landing_path")

    #  Logs successful completion of each step
    def test_log_successful_completion(self, mocker):
        # Write test to setup test data.
        # Mock the necessary dependencies
        mocker.patch('etl.data_jobs.air_asia_data_job.urllib.request.urlopen')
        mocker.patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.get_spark_session')
        mocker.patch('etl.data_jobs.air_asia_data_job.AirADataJob.logger')

        # Initialize the class
        job = AirADataJob("air_asia_data_job")

        # Invoke the method being tested
        job.run()

        # Assert the expected behavior
        job.logger.info.assert_called_with("superman.json file stored at /path/to/superman_landing_path")

    #  Throws an exception if the API or web is not accessible
    def test_throw_exception_if_api_not_accessible(self, mocker):
        # Write test to setup test data.
        # Mock the necessary dependencies
        mocker.patch('etl.data_jobs.air_asia_data_job.urllib.request.urlopen', side_effect=Exception)
        mocker.patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.get_spark_session')
        mocker.patch('etl.data_jobs.air_asia_data_job.AirADataJob.logger')

        # Initialize the class
        job = AirADataJob("air_asia_data_job")

        # Invoke the method being tested
        with pytest.raises(Exception):
            job.ingest_api_data("url", "landing_path")

        # Assert the expected behavior
        job.logger.error.assert_called_once()

    #  Throws an exception if the input path or output path is invalid
    def test_throw_exception_if_invalid_path(self, mocker):
        # Write test to setup test data.
        # Mock the necessary dependencies
        mocker.patch('etl.data_jobs.air_asia_data_job.urllib.request.urlopen')
        mocker.patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.get_spark_session')
        mocker.patch('etl.data_jobs.air_asia_data_job.AirADataJob.logger')

        # Initialize the class
        job = AirADataJob("air_asia_data_job")

        # Invoke the method being tested
        with pytest.raises(IOError):
            job.process_json([], "invalid_path")

        # Assert the expected behavior
        job.logger.error.assert_called_once()

    #  Throws an exception if the json file is not in the expected format
    def test_throw_exception_if_invalid_json_format(self, mocker):
        # Write test to setup test data.
        # Mock the necessary dependencies
        mocker.patch('etl.data_jobs.air_asia_data_job.urllib.request.urlopen')
        mocker.patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.get_spark_session')
        mocker.patch('etl.data_jobs.air_asia_data_job.AirADataJob.logger')

        # Initialize the class
        job = AirADataJob("air_asia_data_job")

        # Invoke the method being tested
        with pytest.raises(IOError):
            job.flatten_json("invalid_path")

        # Assert the expected behavior
        job.logger.error.assert_called_once()
