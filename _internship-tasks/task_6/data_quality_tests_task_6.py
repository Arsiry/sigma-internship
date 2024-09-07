from task_6 import *

def check_null_values(df: DataFrame):
    null_counts = df.select([F.count(F.when(F.col(c).isNull(), c)).alias(c) for c in df.columns])
    print("Null values:")
    null_counts.show()

def check_unique_key(df: DataFrame, key_column: str):
    total_count = df.count()
    distinct_count = df.select(key_column).distinct().count()
    if total_count != distinct_count:
        print(f"Duplicate values found in {key_column}")
    else:
        print(f"{key_column} is unique")

def check_column_range(df: DataFrame, column: str, valid_range: tuple):
    out_of_range = df.filter((F.col(column) < valid_range[0]) | (F.col(column) > valid_range[1]))
    if out_of_range.count() > 0:
        print(f"Values out of range in {column}")
    else:
        print(f"All values in {column} are within the valid range")

def check_timestamp_format(df: DataFrame, column: str, format: str = "yyyy-MM-dd HH:mm:ss"):
    invalid_timestamps = df.filter(~F.to_date(F.col(column), format).isNotNull())
    if invalid_timestamps.count() > 0:
        print(f"Invalid timestamp format in {column}")
    else:
        print(f"All timestamps in {column} are valid")

def check_valid_categories(df: DataFrame, column: str, valid_values: list):
    invalid_values = df.filter(~F.col(column).isin(valid_values))
    if invalid_values.count() > 0:
        print(f"Invalid values found in {column}")
    else:
        print(f"All values in {column} are valid")

# Create Spark Session
spark = create_spark_session()

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
path = "/Users/anastasiiatrofymova/projects/sigma-internship/_internship-tasks/task_6/impressions.csv"
df = spark.read.option("header", True).schema(schema).csv(path)

df.printSchema()

df.show(5)

check_null_values(df)
check_unique_key(df, "impression_id")
check_unique_key(df, "user_id")
check_column_range(df, "is_4G", (0, 1))
check_column_range(df, "is_click", (0, 1))
check_timestamp_format(df, "impression_time")
check_valid_categories(df, "os_version", ["latest", "intermediate", "old"])