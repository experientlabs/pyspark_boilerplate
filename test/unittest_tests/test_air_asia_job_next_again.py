
# Generated by CodiumAI

# Dependencies:
# pip install pytest-mock
import unittest

from pyspark.sql.functions import count, split

from etl.utils.column_constants import Columns


class TestProcessApiData(unittest.TestCase):

    #  Reads csv data from input path
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.air_data_job = None

    def test_reads_csv_data_from_input_path(self, mocker):
        # Mock the necessary dependencies
        mock_spark = mocker.Mock()
        mock_read = mocker.Mock()
        mock_option = mocker.Mock()
        mock_load = mocker.Mock()
        mock_select = mocker.Mock()
        mock_groupby = mocker.Mock()
        mock_agg = mocker.Mock()
        mock_coalesce = mocker.Mock()
        mock_write = mocker.Mock()
        mock_format = mocker.Mock

        # Set up the mocks
        mocker.patch.object(mock_spark, 'read', return_value=mock_read)
        mocker.patch.object(mock_read, 'format', return_value=mock_format)
        mocker.patch.object(mock_format, 'option', return_value=mock_option)
        mocker.patch.object(mock_option, 'load', return_value=mock_load)
        mocker.patch.object(mock_load, 'select', return_value=mock_select)
        mocker.patch.object(mock_select, 'groupby', return_value=mock_groupby)
        mocker.patch.object(mock_groupby, 'agg', return_value=mock_agg)
        mocker.patch.object(mock_agg, 'coalesce', return_value=mock_coalesce)
        mocker.patch.object(mock_coalesce, 'write', return_value=mock_write)

        # Define the input and output paths
        input_path = "path/to/input_file.csv"
        output_path = "path/to/output_folder"

        # Call the process_api_data method
        self.air_data_job.process_api_data(input_path, output_path)

        # Assert that the necessary methods were called with the correct arguments
        mock_read.format.assert_called_once_with("csv")
        mock_option.assert_called_once_with("header", "true")
        mock_load.assert_called_once_with(input_path)
        mock_select.assert_called_once_with(
            Columns.GENDER,
            split("email", "@", -1)[1].alias("email_provider"),
            "username",
        )
        mock_groupby.assert_called_once_with("gender", "email_provider")
        mock_agg.assert_called_once_with(count("username"))
        mock_coalesce.assert_called_once_with(1)
        mock_write.format.assert_called_once_with("csv")
        mock_write.mode.assert_called_once_with("overwrite")
        mock_write.option.assert_called_once_with("header", True)
        mock_write.option.assert_called_once_with("sep", ",")
        mock_write.save.assert_called_once_with(output_path + "/assessment_2_total_count")

    #  Selects gender, email_provider and username columns from the csv data
    def test_selects_columns_from_csv_data(self, mocker):
        # Mock the necessary dependencies
        mock_spark = mocker.Mock()
        mock_read = mocker.Mock()
        mock_option = mocker.Mock()
        mock_load = mocker.Mock()
        mock_select = mocker.Mock()
        mock_groupby = mocker.Mock()
        mock_agg = mocker.Mock()
        mock_coalesce = mocker.Mock()
        mock_write = mocker.Mock()

        # Set up the mocks
        mocker.patch.object(self.air_data_job.spark, 'read', return_value=mock_read)
        mocker.patch.object(mock_read, 'format', return_value=mock_format)
        mocker.patch.object(mock_format, 'option', return_value=mock_option)
        mocker.patch.object(mock_option, 'load', return_value=mock_load)
        mocker.patch.object(mock_load, 'select', return_value=mock_select)
        mocker.patch.object(mock_select, 'groupby', return_value=mock_groupby)
        mocker.patch.object(mock_groupby, 'agg', return_value=mock_agg)
        mocker.patch.object(mock_agg, 'coalesce', return_value=mock_coalesce)
        mocker.patch.object(mock_coalesce, 'write', return_value=mock_write)

        # Define the input and output paths
        input_path = "path/to/input_file.csv"
        output_path = "path/to/output_folder"

        # Call the process_api_data method
        self.air_data_job.process_api_data(input_path, output_path)

        # Assert that the necessary methods were called with the correct arguments
        mock_read.format.assert_called_once_with("csv")
        mock_option.assert_called_once_with("header", "true")
        mock_load.assert_called_once_with(input_path)
        mock_select.assert_called_once_with(
            Columns.GENDER,
            split("email", "@", -1)[1].alias("email_provider"),
            "username",
        )
        mock_groupby.assert_called_once_with("gender", "email_provider")
        mock_agg.assert_called_once_with(count("username"))
        mock_coalesce.assert_called_once_with(1)
        mock_write.format.assert_called_once_with("csv")
        mock_write.mode.assert_called_once_with("overwrite")
        mock_write.option.assert_called_once_with("header", True)
        mock_write.option.assert_called_once_with("sep", ",")
        mock_write.save.assert_called_once_with(output_path + "/assessment_2_total_count")
