# Databricks notebook source
from runtime.nutterfixture import NutterFixture
from pyspark.sql.types import StructField, StructType, LongType

from my_package import (
    generate_data2,
    spark,
)


TABLE_NAME = "my_data"

class IntegrationTest(NutterFixture):
    def __init__(self):
        self.table_name = TABLE_NAME
        NutterFixture.__init__(self)

    def run_pipeline(self):
        generate_data2(spark=spark, table_name=self.table_name)

    def assertion_pipeline(self):
        assert (spark.catalog.tableExists(self.table_name))

    def assertion_pipeline_schema(self):
        schema = StructType([StructField("id", LongType(), True)])
        expected_df = spark.createDataFrame([(42,)], schema=schema)
        df = spark.read.table(self.table_name).limit(1)
        assert (df.schema == expected_df.schema)

    def assertion_pipeline_rows(self):
        some_tbl = spark.sql(
            f"SELECT COUNT(*) AS total FROM {self.table_name}"
        )
        first_row = some_tbl.first()
        assert (first_row[0] == 10)

    def assertion_pipeline_values(self):
        df = spark.sql(f"SELECT * FROM {self.table_name} ORDER BY id LIMIT 1")
        assert (df.first()[0] == 0)


if __name__ == "__main__":
    # Run the tests
    result = IntegrationTest().execute_tests()
    print(result.to_string())

    spark.sql(f"DROP TABLE {TABLE_NAME}")

    # Raise an exception if any of the tests failed
    if result.test_results.num_failures > 0:
        raise Exception("Test failed.")
