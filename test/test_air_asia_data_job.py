# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     15/01/23 11:55 am
# File:             test_air_asia_data_job.py
# -----------------------------------------------------------------------
import unittest

from etl.data_jobs.air_asia_data_job import AirADataJob
from etl.utils import spark_utils
from etl.config import config_utils


class TestAirA(unittest.TestCase):
    """
    TODO: Add test for all functions. Currently it is skeleton only
    """

    utils = spark_utils.SparkUtils()
    spark = utils.get_spark_session("air_asia_data_job")

    config_path = "../etl/config/pipeline.cfg"
    configutil = config_utils.ConfigUtil(config_path)
    configutil.get_config("IO_CONFIGS", "INPUT_DATA_PATH")

    def test_read_superman_json_from_web(self, mocker):
        mocker.patch.object(AirADataJob, 'run', return_value=None)
        job = AirADataJob("air_a_data_job")
        job.aa_helper.read_json_from_web = mocker.Mock()
        job.run()
        job.aa_helper.read_json_from_web.assert_called_once_with(job.json_url, job.superman_landing_path)

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
