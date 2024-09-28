from pyspark.sql import SparkSession, Row, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType
from pyspark.sql import functions as F

from delta import *

def create_spark_session():
    builder = SparkSession.builder \
        .appName("Delta Table Example") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    return spark

def prepare_delta_table(spark):
    # Schema definition
    schema = StructType([
        StructField("impression_id", StringType(), True),
        StructField("impression_time", StringType(), True),
        StructField("user_id", IntegerType(), True),
        StructField("app_code", IntegerType(), True),
        StructField("os_version", StringType(), True),
        StructField("is_4G", IntegerType(), True),
        StructField("is_click", IntegerType(), True)
    ])

    # Load data with schema applied
    path = "/Users/anastasiiatrofymova/projects/sigma-internship/_internship-tasks/task_6_v2/impressions.csv"
    df = spark.read.option("header", True).schema(schema).csv(path)

    # Write DataFrame as Delta table
    df.write.format("delta").mode("overwrite").save("data/impressions_delta_table")


def etl(spark, delta_df):
    # 1. Filter: Impressions for Users only with latest OS
    latest_os_df = delta_df.filter(F.col("os_version") == 'latest')

    # 2. Add New Columns  - Day of Week
    newcolumn_df = latest_os_df.withColumn("dayofweek", F.dayofweek("impression_time"))

    # 3. Aggregate: Total Clicks per Day of Week
    total_clicks_df = newcolumn_df.groupBy("dayofweek",).agg(F.sum("is_click").alias("total_clicks"))
    return total_clicks_df


# Create Spark Session
spark = create_spark_session()

# prepare delta table
prepare_delta_table(spark)

### Data Transformation Pipeline

# Load Delta table
delta_df = spark.read.format("delta").load("data/impressions_delta_table")

# apply ETl transformations
total_clicks_df = etl(spark, delta_df)

# Write the Transformed Data
total_clicks_df.write.format("delta").mode("overwrite").save("data/tranformation_impressions_delta_table")
