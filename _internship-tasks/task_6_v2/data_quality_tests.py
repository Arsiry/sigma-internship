import unittest
from task_6 import *
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

class DataQualityTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = create_spark_session()
        cls.schema = StructType([
            StructField("impression_id", StringType(), True),
            StructField("impression_time", StringType(), True),
            StructField("user_id", IntegerType(), True),
            StructField("app_code", IntegerType(), True),
            StructField("os_version", StringType(), True),
            StructField("is_4G", IntegerType(), True),
            StructField("is_click", IntegerType(), True)
        ])
        cls.path = "/Users/anastasiiatrofymova/projects/sigma-internship/_internship-tasks/task_6_v2/impressions.csv"
        cls.df = cls.spark.read.option("header", True).schema(cls.schema).csv(cls.path)

    # Test to check for null values in each column
    def test_check_null_values(self):
        null_counts = self.df.select([F.sum(F.when(F.col(c).isNull(), 1).otherwise(0)).alias(c) for c in self.df.columns])
        results = null_counts.collect()[0].asDict()

        for col, null_count in results.items():
            self.assertEqual(null_count, 0, f"Null values found in column {col}")

    # Test to check for unique keys in 'impression_id'
    def test_check_unique_key(self):
        impression_count = self.df.count()
        impression_distinct_count = self.df.select("impression_id").distinct().count()

        self.assertEqual(impression_count, impression_distinct_count, "Duplicate values found in 'impression_id'")

    # Test to check if 'is_4G' and 'is_click' columns are within the valid range (0, 1)
    def test_check_column_range(self):
        invalid_is_4G = self.df.filter((F.col("is_4G") < 0) | (F.col("is_4G") > 1)).count()
        invalid_is_click = self.df.filter((F.col("is_click") < 0) | (F.col("is_click") > 1)).count()

        self.assertEqual(invalid_is_4G, 0, "Values out of range in 'is_4G'")
        self.assertEqual(invalid_is_click, 0, "Values out of range in 'is_click'")

    # Test to check if the 'impression_time' column has valid timestamps
    def test_check_timestamp_format(self):
        invalid_timestamps = self.df.filter(~F.to_date(F.col("impression_time"), "yyyy-MM-dd HH:mm:ss").isNotNull()).count()

        self.assertEqual(invalid_timestamps, 0, "Invalid timestamps in 'impression_time'")

    # Test to check if 'os_version' contains valid categories
    def test_check_valid_categories(self):
        valid_values = ["latest", "intermediate", "old"]
        invalid_values = self.df.filter(~F.col("os_version").isin(valid_values)).count()

        self.assertEqual(invalid_values, 0, "Invalid values found in 'os_version'")
