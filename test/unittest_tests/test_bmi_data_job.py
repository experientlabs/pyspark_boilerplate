import unittest
from unittest.mock import Mock, patch
from pyspark.sql import SparkSession
from etl.data_jobs.BMI_data_job import BMIDataJob

class TestBMIDataJob(unittest.TestCase):

    def setUp(self):
        self.mock_spark_session = Mock(spec=SparkSession)
        self.mock_spark_utils = Mock()
        self.mock_logger = Mock()

    @patch('etl.data_jobs.BMI_data_job.spark_utils.SparkUtils', autospec=True)
    @patch('etl.data_jobs.BMI_data_job.Logger', autospec=True)
    @patch('etl.data_jobs.BMI_data_job.config_utils.ConfigUtil', autospec=True)
    def test_init(self, mock_config_util, mock_logger, mock_spark_utils):
        # Arrange
        job_name = "bmi_data_job"

        # Act
        bmi_data_job = BMIDataJob(job_name)

        # Assert
        self.assertEqual(bmi_data_job.job_name, job_name)
        self.assertEqual(bmi_data_job.logger, mock_logger.return_value.get_logger.return_value)
        self.assertEqual(bmi_data_job.spark, mock_spark_utils.return_value.get_spark_session.return_value)

    @patch('etl.data_jobs.bmi_data_job.SparkUtils', autospec=True)
    @patch('etl.data_jobs.bmi_data_job.Logger', autospec=True)
    @patch('etl.data_jobs.bmi_data_job.config_utils.ConfigUtil', autospec=True)
    def test_run(self, mock_config_util, mock_logger, mock_spark_utils):
        # Arrange
        bmi_data_job = BMIDataJob("bmi_data_job")
        mock_read_data = Mock()
        mock_calculate_bmi = Mock()
        mock_get_bmi_category = Mock()
        mock_get_record_count = Mock()
        mock_write_data = Mock()

        with patch.object(bmi_data_job.utils, 'read_data', mock_read_data), \
             patch.object(bmi_data_job, 'calculate_bmi', mock_calculate_bmi), \
             patch.object(bmi_data_job, 'get_bmi_category', mock_get_bmi_category), \
             patch.object(bmi_data_job, 'get_record_count', mock_get_record_count), \
             patch.object(bmi_data_job.utils, 'write_data', mock_write_data):

            # Act
            bmi_data_job.run()

            # Assert
            mock_read_data.assert_called_once_with(bmi_data_job.spark, bmi_data_job.bmi_data, "json")
            mock_calculate_bmi.assert_called_once_with(mock_read_data.return_value)
            mock_get_bmi_category.assert_called_once_with(mock_calculate_bmi.return_value)
            mock_get_record_count.assert_called_once_with(mock_get_bmi_category.return_value)
            mock_write_data.assert_called_once_with(mock_get_bmi_category.return_value, bmi_data_job.bmi_data_target, "json")
            self.mock_logger.info.assert_called_with("Data processing completed")

    @patch('etl.data_jobs.bmi_data_job.SparkUtils', autospec=True)
    @patch('etl.data_jobs.bmi_data_job.Logger', autospec=True)
    @patch('etl.data_jobs.bmi_data_job.config_utils.ConfigUtil', autospec=True)
    def test_calculate_bmi(self, mock_config_util, mock_logger, mock_spark_utils):
        # Arrange
        bmi_data_job = BMIDataJob("bmi_data_job")
        mock_df = Mock()
        expected_df = Mock()
        mock_df.withColumn.return_value.withColumn.return_value = expected_df

        # Act
        result = bmi_data_job.calculate_bmi(mock_df)

        # Assert
        mock_df.withColumn.assert_called_with("HeightM", mock_df.HeightCm / 100)
        mock_df.withColumn.return_value.withColumn.assert_called_with(
            "BMI",
            round(mock_df.WeightKg / ((mock_df.HeightCm / 100) * (mock_df.HeightCm / 100)), 2)
        )
        self.assertEqual(result, expected_df)

    @patch('etl.data_jobs.bmi_data_job.SparkUtils', autospec=True)
    @patch('etl.data_jobs.bmi_data_job.Logger', autospec=True)
    @patch('etl.data_jobs.bmi_data_job.config_utils.ConfigUtil', autospec=True)
    def test_get_bmi_category(self, mock_config_util, mock_logger, mock_spark_utils):
        # Arrange
        bmi_data_job = BMIDataJob("bmi_data_job")
        mock_df = Mock()
        expected_df = Mock()
        mock_df.withColumn.return_value.withColumn.return_value = expected_df

        # Act
        result = bmi_data_job.get_bmi_category(mock_df)

        # Assert
        mock_df.withColumn.assert_called_with(
            "BMI Category",
            when(mock_df.BMI <= 18.4, "Underweight")
            .when((mock_df.BMI >= 18.5) & (mock_df.BMI <= 24.9), "Normal weight")
            .when((mock_df.BMI >= 25) & (mock_df.BMI <= 29.9), "Overweight")
            .when((mock_df.BMI >= 30) & (mock_df.BMI <= 34.9), "Moderately obese")
            .when((mock_df.BMI >= 35) & (mock_df.BMI <= 39.9), "Severely obese")
            .when((mock_df.BMI >= 40), "Very severely obese")
            .otherwise("Undefined")
        )
        mock_df.withColumn.return_value.withColumn.assert_called_with(
            "Health risk",
            when(mock_df.BMI <= 18.4, "Malnutrition risk")
            .when((mock_df.BMI >= 18.5) & (mock_df.BMI <= 24.9), "Low risk")
            .when((mock_df.BMI >= 25) & (mock_df.BMI <= 29.9), "Enhanced risk")
            .when((mock_df.BMI >= 30) & (mock_df.BMI <= 34.9), "Medium risk")
            .when((mock_df.BMI >= 35) & (mock_df.BMI <= 39.9), "High risk")
            .when((mock_df.BMI >= 40), "Very high risk")
            .otherwise("Undefined")
        )
        self.assertEqual(result, expected_df)

    @patch('etl.data_jobs.bmi_data_job.SparkUtils', autospec=True)
    @patch('etl.data_jobs.bmi_data_job.Logger', autospec=True)
    @patch('etl.data_jobs.bmi_data_job.config_utils.ConfigUtil', autospec=True)
    def test_get_record_count(self, mock_config_util, mock_logger, mock_spark_utils):
        # Arrange
        bmi_data_job = BMIDataJob("bmi_data_job")
        mock_df = Mock()
        mock_df.filter.return_value.count.return_value = 42

        # Act
        result = bmi_data_job.get_record_count(mock_df)

        # Assert
        mock_df.filter.assert_called_with(col("BMI Category") == "Overweight")
        mock_df.filter.return_value.count.assert_called_once()
        self.assertEqual(result, 42)

if __name__ == "__main__":
    unittest.main()
