import unittest
from pyspark.sql import SparkSession, Row, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType
from task_6 import create_spark_session, etl  

class TestETL(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # We create a Spark session once for all tests
        cls.spark = create_spark_session()
        cls.input_schema = StructType([
            StructField("impression_id", StringType(), True),
            StructField("impression_time", StringType(), True),
            StructField("user_id", IntegerType(), True),
            StructField("app_code", IntegerType(), True),
            StructField("os_version", StringType(), True),
            StructField("is_4G", IntegerType(), True),
            StructField("is_click", IntegerType(), True)
        ])

    def assert_dataframe_equal(self, df1: DataFrame, df2: DataFrame):
        # Comparison of two DataFrames based on schema and data
        self.assertEqual(df1.schema, df2.schema, "Schemas do not match")
        self.assertEqual(sorted(df1.collect()), sorted(df2.collect()), "DataFrames content does not match")

    def test_case_1(self):
        # Arrange
        input = [
            ("qw3er4ty5", "2024-01-02 01:22:00", 101, 11, "old", 0, 1),
            ("fhfgf6hfh", "2024-01-03 01:22:00", 102, 22, "latest", 1, 1),
            ("gfgdhd664", "2024-01-03 01:22:00", 103, 33, "intermediate", 0, 1),
            ("hdhdjms45", "2024-01-05 01:22:00", 103, 22, "latest", 0, 1),
            ("363gfcf66", "2024-01-05 01:22:00", 105, 11, "latest", 1, 1)
        ]
        input_df = self.spark.createDataFrame(input, self.input_schema)

        # Act
        actual_df = etl(self.spark, input_df)

        # Assert
        expected_data = [
            Row(dayofweek=4, total_clicks=1),
            Row(dayofweek=6, total_clicks=2)
        ]
        expected_schema = StructType([
            StructField("dayofweek", IntegerType(), True),
            StructField("total_clicks", LongType(), True)
        ])
        expected_df = self.spark.createDataFrame(expected_data, expected_schema)

        # Assert DataFrames are equal
        self.assert_dataframe_equal(actual_df, expected_df)

    def test_case_2(self):
        # Arrange
        input = [
            ("id001", "2024-03-01 09:00:00", 301, 12, "old", 1, 0),
            ("id002", "2024-03-02 10:15:00", 302, 34, "latest", 0, 1),
            ("id003", "2024-03-02 12:30:00", 303, 56, "intermediate", 1, 1),
            ("id004", "2024-03-03 14:45:00", 304, 78, "latest", 0, 0),
            ("id005", "2024-03-03 16:00:00", 305, 12, "latest", 1, 1),
            ("id006", "2024-03-04 18:15:00", 306, 34, "old", 0, 0),
            ("id007", "2024-03-05 20:30:00", 307, 56, "latest", 1, 1),
            ("id008", "2024-03-05 22:45:00", 308, 78, "intermediate", 0, 0),
            ("id009", "2024-03-06 07:00:00", 309, 12, "latest", 0, 1),
            ("id010", "2024-03-06 08:30:00", 310, 34, "latest", 1, 1)
        ]
        input_df = self.spark.createDataFrame(input, self.input_schema)

        # Act
        actual_df = etl(self.spark, input_df)

        # Assert
        expected_data = [
            Row(dayofweek=1, total_clicks=1),
            Row(dayofweek=3, total_clicks=1),
            Row(dayofweek=4, total_clicks=2),
            Row(dayofweek=7, total_clicks=1)
        ]
        expected_schema = StructType([
            StructField("dayofweek", IntegerType(), True),
            StructField("total_clicks", LongType(), True)
        ])
        expected_df = self.spark.createDataFrame(expected_data, expected_schema)

        # Assert DataFrames are equal
        self.assert_dataframe_equal(actual_df, expected_df)

    def test_empty_data(self):
        # Arrange
        input = []
        input_df = self.spark.createDataFrame(input, self.input_schema)

        # Act
        actual_df = etl(self.spark, input_df)

        # Assert
        expected_data = []
        expected_schema = StructType([
            StructField("dayofweek", IntegerType(), True),
            StructField("total_clicks", LongType(), True)
        ])
        expected_df = self.spark.createDataFrame(expected_data, expected_schema)

        # Assert DataFrames are equal
        self.assert_dataframe_equal(actual_df, expected_df)
