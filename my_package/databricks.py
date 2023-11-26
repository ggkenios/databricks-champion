from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import DataFrame


def running_on_databricks(env_var: str = "DATABRICKS_RUNTIME_VERSION") -> bool:
    """Check if the code is running on Databricks."""
    import os

    environment_var = os.getenv(env_var, None)
    if environment_var:
        return True
    else:
        return False


def display(df: DataFrame) -> None:
    """Display a dataframe."""
    if running_on_databricks():
        return df.display()
    else:
        return df.show()


def get_spark_session() -> SparkSession:
    """Create a SparkSession."""
    if running_on_databricks():
        spark = SparkSession.builder.getOrCreate()
    else:
        import findspark

        findspark.init()

        conf = SparkConf()
        sc = SparkContext(conf=conf)
        spark = SparkSession(sc)
    return spark


spark = get_spark_session()
