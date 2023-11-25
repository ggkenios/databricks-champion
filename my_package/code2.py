from pyspark.sql import SparkSession


def generate_data2(spark: SparkSession, table_name: str = "my_data") -> None:
    df = spark.range(0,10)
    df.write.format("delta").mode("overwrite").saveAsTable(table_name)
