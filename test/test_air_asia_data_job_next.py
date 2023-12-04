import unittest
from unittest.mock import patch, Mock
from etl.data_jobs.air_asia_data_job import AirADataJob


class TestAirADataJob(unittest.TestCase):

    #  Successfully read superman.json file from web and stored it at the landing path
    @patch.object(AirADataJob, 'run', return_value=None)
    def test_read_superman_json_from_web(self, mock_run):
        job = AirADataJob("air_a_data_job")
        job.aa_helper.read_json_from_web = Mock()
        job.run()
        job.aa_helper.read_json_from_web.assert_called_once_with(job.json_url, job.superman_landing_path)

    #  Successfully read data from random user API and dumped the dataset at the landing path
    def test_ingest_api_data(self, mocker):
        mocker.patch.object(AirADataJob, 'run', return_value=None)
        job = AirADataJob("air_a_data_job")
        job.aa_helper.ingest_api_data = mocker.Mock()
        job.run()
        job.aa_helper.ingest_api_data.assert_called_once_with(job.url, job.random_user_landing_path)

    #  Processed json data and created superman_final.json
    def test_process_json(self, mocker):
        mocker.patch.object(AirADataJob, 'run', return_value=None)
        job = AirADataJob("air_a_data_job")
        job.flatten_json = mocker.Mock(return_value=['{"name": "John"}', '{"name": "Jane"}'])
        job.process_json = mocker.Mock()
        job.run()
        job.flatten_json.assert_called_once_with(job.superman_landing_path)
        job.process_json.assert_called_once_with(['{"name": "John"}', '{"name": "Jane"}'], job.superman_target_path)

    #  Invalid URL for reading superman.json file from web
    def test_invalid_superman_json_url(self, mocker):
        mocker.patch.object(AirADataJob, 'run', return_value=None)
        job = AirADataJob("air_a_data_job")
        job.json_url = "invalid_url"
        with self.assertRaises(Exception):
            job.run()

    #  Invalid URL for reading data from random user API
    def test_invalid_random_user_api_url(self, mocker):
        mocker.patch.object(AirADataJob, 'run', return_value=None)
        job = AirADataJob("air_a_data_job")
        job.url = "invalid_url"
        with self.assertRaises(Exception):
            job.run()

    #  Invalid path for storing superman.json file
    def test_invalid_superman_landing_path(self, mocker):
        mocker.patch.object(AirADataJob, 'run', return_value=None)
        job = AirADataJob("air_a_data_job")
        job.superman_landing_path = "/invalid/path"
        with self.assertRaises(Exception):
            job.run()
