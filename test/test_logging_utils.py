# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/01/23 7:39 pm
# File:             test_logging_utils.py.py
# -----------------------------------------------------------------------
import os
import unittest
from etl.utils.logging_utils import Logger
from project_root_dir import project_root_dir


class TestLoggingUtils(unittest.TestCase):
    def test_log_path(self):
        logger = Logger("test")
        log_path = logger.LOG_DIRECTORY
        absolute_path = os.path.abspath(log_path)
        assert absolute_path == project_root_dir+ "/logs"

    def test_get_old_logs(self):
        """
        TODO: To complete this function
        :return:
        """

    def test_get_log_file_name(self):
        """
        TODO: To complete this function
        :return:
        """


if __name__ == "__main__":
    unittest.main()
