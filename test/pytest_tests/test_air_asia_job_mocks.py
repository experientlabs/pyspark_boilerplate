import os.path

import pytest

from etl.data_jobs.air_asia_data_job import AirADataJob


class TestAirADataJob:

    #  Reading superman.json file from web and storing it at the landing path
    def test_read_superman_json_from_web(self, mocker):
        mocker.patch.object(AirADataJob, 'run')
        job = AirADataJob("air_asia_data_job")
        job.aa_helper.read_json_from_web = mocker.Mock(return_value=None)
        job.run()
        job.aa_helper.read_json_from_web.assert_called_once_with(job.json_url, job.superman_landing_path)

    #  Flattening json data
    def test_flatten_json(self, mocker):

        mocker.patch.object(AirADataJob, 'run')
        job = AirADataJob("air_asia_data_job")
        test_path = os.path.abspath(job.superman_landing_path).replace("test/pytest_tests", "")
        print("++++++++++++++++++++++")
        print(os.path.abspath(job.superman_landing_path))
        print(os.path.abspath(test_path))
        job.flatten_json(test_path)
        assert job.flatten_json(job.superman_landing_path) == ['{"name": "Clark Kent", "alias": "Superman", "powers": ["super strength", "flight", "invulnerability"]}', '{"name": "Bruce Wayne", "alias": "Batman", "powers": ["intelligence", "wealth", "martial arts"]}', '{"name": "Diana Prince", "alias": "Wonder Woman", "powers": ["super speed", "super strength", "lasso of truth"]}', '{"name": "Barry Allen", "alias": "The Flash", "powers": ["super speed", "time travel", "speed force"]}', '{"name": "Arthur Curry", "alias": "Aquaman", "powers": ["super strength", "underwater breathing", "telepathy"]}']

    #  Processing json data and creating superman_final.json
    def test_process_json(self, mocker):
        mocker.patch.object(AirADataJob, 'run')
        job = AirADataJob("air_asia_data_job")
        job.process_json(['{"name": "Clark Kent", "alias": "Superman", "powers": ["super strength", "flight", "invulnerability"]}', '{"name": "Bruce Wayne", "alias": "Batman", "powers": ["intelligence", "wealth", "martial arts"]}', '{"name": "Diana Prince", "alias": "Wonder Woman", "powers": ["super speed", "super strength", "lasso of truth"]}', '{"name": "Barry Allen", "alias": "The Flash", "powers": ["super speed", "time travel", "speed force"]}', '{"name": "Arthur Curry", "alias": "Aquaman", "powers": ["super strength", "underwater breathing", "telepathy"]}'], job.superman_target_path)
        assert job.process_json(['{"name": "Clark Kent", "alias": "Superman", "powers": ["super strength", "flight", "invulnerability"]}', '{"name": "Bruce Wayne", "alias": "Batman", "powers": ["intelligence", "wealth", "martial arts"]}', '{"name": "Diana Prince", "alias": "Wonder Woman", "powers": ["super speed", "super strength", "lasso of truth"]}', '{"name": "Barry Allen", "alias": "The Flash", "powers": ["super speed", "time travel", "speed force"]}', '{"name": "Arthur Curry", "alias": "Aquaman", "powers": ["super strength", "underwater breathing", "telepathy"]}'], job.superman_target_path) == None

    #  Invalid URL for reading superman.json file from web
    def test_invalid_url_read_superman_json_from_web(self, mocker):
        mocker.patch.object(AirADataJob, 'run')
        job = AirADataJob("air_asia_data_job")
        job.aa_helper.read_json_from_web = mocker.Mock(side_effect=Exception("Invalid URL"))
        with pytest.raises(Exception):
            job.run()

    #  Invalid URL for reading random user data from API
    def test_invalid_url_ingest_api_data(self, mocker):
        mocker.patch.object(AirADataJob, 'run')
        job = AirADataJob("air_asia_data_job")
        job.aa_helper.ingest_api_data = mocker.Mock(side_effect=Exception("Invalid URL"))
        with pytest.raises(Exception):
            job.run()
