from pyspark.sql import SparkSession


def generate_data2(table_name: str = "my_data"):
    df = SparkSession.getActiveSession().range(0,10)
    df.write.format("delta").mode("overwrite").saveAsTable(table_name)
