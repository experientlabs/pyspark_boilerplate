# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     14/01/23 9:17 pm
# File:             config_utils.py
# -----------------------------------------------------------------------
import configparser
import os

from project_root_dir import project_root_dir
from etl.utils.logging_utils import Logger


class ConfigUtil:
    """
    This class provides access to pipeline configs stored in pipeline.cfg
    """

    def __init__(self, config_path: str = project_root_dir + "/etl/config/pipeline.cfg"):
        self.cfg_path = config_path

    logger = Logger(__name__).get_logger()

    def get_config(self, section: str, config_name: str) -> str:
        """
        This function reads config file and returns values
        :param section:             Config file section to read
        :param config_name:         Config name
        :return:                    returns value of the config
        """
        try:
            config = configparser.ConfigParser()
            config.read(self.cfg_path)
            if config_name.__contains__("URL"):
                return config.get(section, config_name)
            return project_root_dir + "/" + config.get(section, config_name)
        except IOError as exp:
            self.logger.error(f"error reading config file {str(exp)}")


# if __name__ == '__main__':
#     path = project_root_dir
#     print(path)
    # configutil = ConfigUtil()
    # landing_path = configutil.get_config("IO_CONFIGS", "AA_LANDING_PATH")
    # print(landing_path)




