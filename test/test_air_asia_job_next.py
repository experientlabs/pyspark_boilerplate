import os
import unittest
from unittest.mock import patch, Mock

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, count

from etl.config.config_utils import ConfigUtil
from etl.data_jobs.air_asia_data_job import AirADataJob
from etl.utils.column_constants import Columns


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

        config_util = ConfigUtil()
        landing_path = config_util.get_config("IO_CONFIGS", "AA_LANDING_PATH")
        target_path = config_util.get_config("IO_CONFIGS", "AA_TARGET_PATH")
        api_landing_path = config_util.get_config("IO_CONFIGS", "AA_API_LANDING_PATH")
        sm_url = config_util.get_config("IO_CONFIGS", "AA_SUPERMAN_JSON_URL")
        ru_url = config_util.get_config("IO_CONFIGS", "AA_RANDOM_USER_URL")
        ru_csv_file = config_util.get_config("FILE_NAMES", "RU_CSV")
        sm_json_file = config_util.get_config("FILE_NAMES", "SM_JSON")
        processed_csv = config_util.get_config("FILE_NAMES", "PR_CSV")

        mock_config_util_instance.get_config.side_effect = [landing_path, ru_csv_file, sm_json_file,
                                                            processed_csv,
                                                            sm_url, ru_url]
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
        print("Calls to mock_logger:", mock_logger.instance.info.call_arg_list)
        print("\n\n")

        # Assert
        mock_logger.assert_called_once_with(job_name)
        mock_read_json_from_web.assert_called_with(sm_url, landing_path)
        print("Calls to mock_logger:", mock_logger.call_arg_list)
        # mock_logger_instance.info.assert_called_with("reading superman.json file from web")
        # mock_logger_instance.info.assert_called_with("superman.json file stored at superman.json")
        mock_flatten_json.assert_called_with(landing_path)
        mock_process_json.assert_called_with(["flattened_data"], target_path)
        # mock_logger_instance.info.assert_called_with("Reading random user data from API")
        mock_ingest_api_data.assert_called_with(ru_url, api_landing_path)
        # mock_logger_instance.info.assert_called_with("dataset dumped on random_user_data.csv")
        mock_process_api_data.assert_called_with(api_landing_path, target_path)
        # mock_logger_instance.info.assert_called_with("placed process data at processed_data.csv")
        # Assert total call count
        total_call_count = (mock_logger.call_count + mock_read_json_from_web.call_count + mock_flatten_json.call_count +
                            mock_process_json.call_count + mock_ingest_api_data.call_count +
                            mock_process_api_data.call_count)
        self.assertEqual(total_call_count, 6)

# ============================================================================================
# =================================== Fix This Code Below ====================================
# ============================================================================================

    # @patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.get_spark_session')
    # @patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.write_data')
    # def test_reads_csv_data_from_input_path(self, mock_write_data, mock_get_spark_session,
    #                                         # mock_config_util, mock_logger
    #                                         ):
    #     # Mock the necessary dependencies
    #     # mock_spark_session = Mock()
    #     # mock_spark_context = Mock()
    #     mock_spark_session = Mock(spec=SparkSession)
    #     mock_spark_context = Mock(spec=SparkContext)
    #     mock_get_spark_session.return_value = mock_spark_session
    #     mock_write_data.return_value = None
    #     mock_read = Mock()
    #     mock_option = Mock()
    #     mock_load = Mock()
    #     mock_spark_session.return_value = mock_read
    #     mock_read.format.return_value = mock_option
    #     mock_option.option.return_value = mock_load
    #     mock_load.load.return_value = Mock()
    #     mock_spark_session.sparkContext = mock_spark_context
    #
    #     # Creating an instance of AirADataJob
    #     air_data_job = AirADataJob("air_asia_data_job")
    #
    #     air_data_job.spark = mock_spark_session
    #     # air_data_job.spark._jsc = mock_spark_context
    #
    #     # Define the input and output paths
    #     input_path = air_data_job.random_user_landing_path
    #     output_path = air_data_job.random_user_target_path
    #
    #     print("Before calling process_api_data")
    #     # Calling the process_api_data method
    #     air_data_job.process_api_data(input_path, output_path)
    #
    #     print("After calling process_api_data")

        # Assertions
        # mock_get_spark_session.assert_called_once()  # Ensure get_spark_session is called
        # mock_spark_session.read.format().option().load.assert_called_once_with(
        #     input_path)  # Adjust as per your actual code
        # mock_spark_session.select().groupby().agg().coalesce().write.format().save.assert_called_once_with(
        #     output_path)  # Adjust as per your actual code
        # mock_write_data.assert_called_once()  # Ensure write_data is called

        # --
        # mock_get_spark_session.assert_called_once()  # Ensure get_spark_session is called
        # mock_read.format.assert_called_once_with("csv")
        # mock_option.option.assert_called_once_with("header", "true")
        # mock_load.load.assert_called_once_with(input_path)  # Adjust based on your actual code
        # mock_write_data.assert_called_once()  # Ensure write_data is called



        # Assert that the necessary methods were called with the correct arguments
        # mock_read.format.assert_called_once_with("csv")
        # mock_option.assert_called_once_with("header", "true")
        # mock_load.assert_called_once_with(input_path)
        # mock_select.assert_called_once_with(
        #     Columns.GENDER,
        #     split("email", "@", -1)[1].alias("email_provider"),
        #     "username",
        # )
        # mock_groupby.assert_called_once_with("gender", "email_provider")
        # mock_agg.assert_called_once_with(count("username"))
        # mock_coalesce.assert_called_once_with(1)
        # mock_write.format.assert_called_once_with("csv")
        # mock_write.mode.assert_called_once_with("overwrite")
        # mock_write.option.assert_called_once_with("header", True)
        # mock_write.option.assert_called_once_with("sep", ",")
        # mock_write.save.assert_called_once_with(output_path + "/assessment_2_total_count")


# ============================================================================================
# ===================================Backup code for lookup===================================
# ============================================================================================

    # @patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.get_spark_session')
    # @patch('etl.data_jobs.air_asia_data_job.spark_utils.SparkUtils.write_data')
    # def test_process_api_data(self, mock_get_spark_session, mock_write_data):
    #     # Mocking dependencies and setting up mocks
    #     mock_spark_session = Mock()
    #     mock_get_spark_session.return_value = mock_spark_session
    #
    #
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
    #     # Define the input and output paths
    #
    #     # Calling the process_api_data method
    #     air_data_job.process_api_data("input_path", "output_path")
    #
    #     # Asserting that the mocked methods were called as expected
    #     # mock_spark_session.read.format.assert_called_with("csv")
    #     # mock_df.select.assert_called_with(
    #     #     'GENDER',
    #     #     split('email', '@')[1].alias('email_provider'),
    #     #     'username'
    #     # )
    #     # mock_df1.groupby.assert_called_with('gender', 'email_provider')
    #     # mock_df2.coalesce(1).write.format.assert_called_with("csv")
    #     # mock_save_dataframe_as_csv.assert_called_with(mock_df2, 'output_path/assessment_2_total_count')
    #     #
    #     mock_groupby.assert_called_once_with("gender", "email_provider")
    #     mock_agg.assert_called_once_with(count("username"))
    #     mock_coalesce.assert_called_once_with(1)
    #     mock_write.format.assert_called_once_with("csv")
    #     mock_write.mode.assert_called_once_with("overwrite")
    #     mock_write.option.assert_called_once_with("header", True)
    #     mock_write.option.assert_called_once_with("sep", ",")
    #     mock_write.save.assert_called_once_with(output_path + "/assessment_2_total_count")
    #
