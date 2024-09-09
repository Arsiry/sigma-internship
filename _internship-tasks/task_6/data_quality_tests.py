from task_6 import *

spark = create_spark_session()

def test_check_null_values():
    # Arrange
    schema = StructType([
        StructField("impression_id", StringType(), True),
        StructField("impression_time", StringType(), True),
        StructField("user_id", IntegerType(), True),
        StructField("app_code", IntegerType(), True),
        StructField("os_version", StringType(), True),
        StructField("is_4G", IntegerType(), True),
        StructField("is_click", IntegerType(), True)
    ])
    path = "/Users/anastasiiatrofymova/projects/sigma-internship/_internship-tasks/task_6/impressions.csv"
    df = spark.read.option("header", True).schema(schema).csv(path)

    # Act
    """Test to check for null values in each column"""
    null_counts = df.select([F.sum(F.when(F.col(c).isNull(), 1).otherwise(0)).alias(c) for c in df.columns])
    results = null_counts.collect()[0].asDict()

    # Assert
    for col, null_count in results.items():
        assert null_count == 0, f"Null values found in column {col}"

def test_check_unique_key():
    # Arrange
    schema = StructType([
        StructField("impression_id", StringType(), True),
        StructField("impression_time", StringType(), True),
        StructField("user_id", IntegerType(), True),
        StructField("app_code", IntegerType(), True),
        StructField("os_version", StringType(), True),
        StructField("is_4G", IntegerType(), True),
        StructField("is_click", IntegerType(), True)
    ])
    path = "/Users/anastasiiatrofymova/projects/sigma-internship/_internship-tasks/task_6/impressions.csv"
    df = spark.read.option("header", True).schema(schema).csv(path)

    # Act
    """Test to check for unique keys in 'impression_id'"""
    impression_count = df.count()
    impression_distinct_count = df.select("impression_id").distinct().count()
    
    # Assert
    assert impression_count == impression_distinct_count, "Duplicate values found in 'impression_id'"


def test_check_column_range():
    # Arrange
    schema = StructType([
        StructField("impression_id", StringType(), True),
        StructField("impression_time", StringType(), True),
        StructField("user_id", IntegerType(), True),
        StructField("app_code", IntegerType(), True),
        StructField("os_version", StringType(), True),
        StructField("is_4G", IntegerType(), True),
        StructField("is_click", IntegerType(), True)
    ])
    path = "/Users/anastasiiatrofymova/projects/sigma-internship/_internship-tasks/task_6/impressions.csv"
    df = spark.read.option("header", True).schema(schema).csv(path)

    # Act
    """Test to check if 'is_4G' and 'is_click' columns are within the valid range (0, 1)"""
    invalid_is_4G = df.filter((F.col("is_4G") < 0) | (F.col("is_4G") > 1)).count()
    invalid_is_click = df.filter((F.col("is_click") < 0) | (F.col("is_click") > 1)).count()

    # Assert
    assert invalid_is_4G == 0, "Values out of range in 'is_4G'"
    assert invalid_is_click == 0, "Values out of range in 'is_click'"


def test_check_timestamp_format():
    # Arrange
    schema = StructType([
        StructField("impression_id", StringType(), True),
        StructField("impression_time", StringType(), True),
        StructField("user_id", IntegerType(), True),
        StructField("app_code", IntegerType(), True),
        StructField("os_version", StringType(), True),
        StructField("is_4G", IntegerType(), True),
        StructField("is_click", IntegerType(), True)
    ])
    path = "/Users/anastasiiatrofymova/projects/sigma-internship/_internship-tasks/task_6/impressions.csv"
    df = spark.read.option("header", True).schema(schema).csv(path)

    # Act
    """Test to check if the 'impression_time' column has valid timestamps"""
    invalid_timestamps = df.filter(~F.to_date(F.col("impression_time"), "yyyy-MM-dd HH:mm:ss").isNotNull()).count()

    # Assert
    assert invalid_timestamps == 0, "Invalid timestamps in 'impression_time'"


def test_check_valid_categories():
    # Arrange
    schema = StructType([
        StructField("impression_id", StringType(), True),
        StructField("impression_time", StringType(), True),
        StructField("user_id", IntegerType(), True),
        StructField("app_code", IntegerType(), True),
        StructField("os_version", StringType(), True),
        StructField("is_4G", IntegerType(), True),
        StructField("is_click", IntegerType(), True)
    ])
    path = "/Users/anastasiiatrofymova/projects/sigma-internship/_internship-tasks/task_6/impressions.csv"
    df = spark.read.option("header", True).schema(schema).csv(path)

    # Act
    """Test to check if 'os_version' contains valid categories"""
    valid_values = ["latest", "intermediate", "old"]
    invalid_values = df.filter(~F.col("os_version").isin(valid_values)).count()

    # Assert
    assert invalid_values == 0, "Invalid values found in 'os_version'"

