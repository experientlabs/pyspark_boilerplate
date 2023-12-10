import os
import unittest
from unittest.mock import patch, Mock
from etl.data_jobs.air_asia_data_job import AirADataJob

class TestAirADataJob(unittest.TestCase):

    @patch('etl.data_jobs.air_asia_data_job.AirAHelper.read_json_from_web')
    @patch('etl.data_jobs.air_asia_data_job.AirADataJob.flatten_json')
    @patch('etl.data_jobs.air_asia_data_job.AirADataJob.process_json')
    @patch('etl.data_jobs.air_asia_data_job.AirAHelper.ingest_api_data')
    @patch('etl.data_jobs.air_asia_data_job.AirADataJob.process_api_data')
    @patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.get_spark_session')
    @patch('etl.data_jobs.air_asia_data_job.config_utils.ConfigUtil')
    @patch('etl.data_jobs.air_asia_data_job.Logger')
    def test_run(self, mock_logger, mock_config_util, mock_get_spark_session, mock_process_api_data,
                 mock_ingest_api_data, mock_process_json, mock_flatten_json, mock_read_json_from_web):
        # Arrange
        job_name = "air_asia_data_job"
        air_data_job = AirADataJob(job_name)
        mock_spark_session = Mock()
        mock_get_spark_session.return_value = mock_spark_session
        mock_logger_instance = mock_logger.return_value.get_logger.return_value
        mock_logger.return_value.get_logger.side_effect = [mock_logger_instance, Mock()]
        mock_config_util_instance = mock_config_util.return_value
        mock_config_util_instance.get_config.side_effect = ["resources/data/source_data/aa_data", "random_user_data.csv",
                                                            "superman_final.json", "processed_data.csv",
                                                            "https://gitlab.com/im-batman/simple-data-assestment/-/raw/main/superman.json",
                                                            "https://randomuser.me/api/0.8/?results=100"]
        mock_read_json_from_web.side_effect = [None, None]
        mock_flatten_json.return_value = ["flattened_data"]
        mock_process_json.return_value = None
        mock_ingest_api_data.return_value = None
        mock_process_api_data.return_value = None

        # Act
        air_data_job.run()

        # Debug print statement
        print("\n\nCalls to mock_read_json_from_web:", mock_read_json_from_web.call_args_list)
        print("Calls to mock_flatten_json:", mock_flatten_json.call_args_list)
        print("Calls to mock_logger:", mock_logger.return_value)
        print("Calls to mock_logger:", mock_logger.call_arg_list)
        print("\n\n")

        # Assert
        mock_logger.assert_called_once_with(job_name)
        mock_read_json_from_web.assert_called_with(
            "https://gitlab.com/im-batman/simple-data-assestment/-/raw/main/superman.json", "resources/data/source_data/aa_data")
        print("Calls to mock_logger:", mock_logger.call_arg_list)
        # mock_logger_instance.info.assert_called_with("reading superman.json file from web")
        # mock_logger_instance.info.assert_called_with("superman.json file stored at superman.json")
        mock_flatten_json.assert_called_with("resources/data/source_data/aa_data")
        mock_process_json.assert_called_with(["flattened_data"], "resources/data/target_data/aa_data")
        # mock_logger_instance.info.assert_called_with("Reading random user data from API")
        mock_ingest_api_data.assert_called_with("https://randomuser.me/api/0.8/?results=100", "resources/data/source_data/aa_data/api_landing_path")
        # mock_logger_instance.info.assert_called_with("dataset dumped on random_user_data.csv")
        mock_process_api_data.assert_called_with("resources/data/source_data/aa_data/api_landing_path", "resources/data/target_data/aa_data")
        # mock_logger_instance.info.assert_called_with("placed process data at processed_data.csv")

    # @patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.get_spark_session')
    # @patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.save_dataframe_as_csv')
    # def test_process_api_data(self, mock_get_spark_session, mock_save_dataframe_as_csv):
    #     # Mocking dependencies and setting up mocks
    #     mock_spark_session = Mock()
    #     mock_get_spark_session.return_value = mock_spark_session
    #     mock_df = Mock()
    #     mock_df1 = Mock()
    #     mock_df2 = Mock()
    #     mock_spark_session.read.format.return_value.option.return_value.load.return_value = mock_df
    #     mock_df.select.return_value = mock_df1
    #     mock_df1.groupby.return_value.agg.return_value = mock_df2
    #
    #     # Creating an instance of AirADataJob
    #     air_data_job = AirADataJob("air_asia_data_job")
    #
    #     # Calling the process_api_data method
    #     air_data_job.process_api_data("input_path", "output_path")
    #
    #     # Asserting that the mocked methods were called as expected
    #     mock_spark_session.read.format.assert_called_with("csv")
    #     mock_df.select.assert_called_with(
    #         'GENDER',
    #         split('email', '@')[1].alias('email_provider'),
    #         'username'
    #     )
    #     mock_df1.groupby.assert_called_with('gender', 'email_provider')
    #     mock_df2.coalesce(1).write.format.assert_called_with("csv")
    #     mock_save_dataframe_as_csv.assert_called_with(mock_df2, 'output_path/assessment_2_total_count')


