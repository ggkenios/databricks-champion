# Databricks notebook source
from runtime.nutterfixture import NutterFixture
from chispa import assert_df_equality

from my_package import (
    generate_data1,
    generate_data2,
    upper_columns,
    spark,
)


TABLE_NAME_1 = "my_cool_data"
TABLE_NAME_2 = "my_data"
COUNT_1 = 100
COUNT_2 = 10


class UnitTest(NutterFixture):
    def __init__(self):
        self.table_name_1 = TABLE_NAME_1
        self.table_name_2 = TABLE_NAME_2
        self.count_1 = COUNT_1
        self.count_2 = COUNT_2
        NutterFixture.__init__(self)

    def run_code1_percent_run(self):
        generate_data1(
            spark=spark,
            table_name=self.table_name_1,
            n=self.count_1,
        )

    def assertion_code1_percent_run(self):
        df = spark.read.table(self.table_name_1)
        assert df.count() == self.count_1

    def run_code2_percent_run(self):
        generate_data2(spark=spark, table_name=self.table_name_2)

    def assertion_code2_percent_run(self):
        df = spark.sql(f"SELECT COUNT(*) AS total FROM {self.table_name_2}")
        assert df.first[0] == self.count_2

    def after_code2_percent_run(self):
        spark.sql(f"DROP TABLE {self.table_name_2}")

    def assertion_upper_columns_percent_run(self):
        cols = ["col1", "col2", "col3"]
        df = spark.createDataFrame([("abc", "cef", 1)], cols)
        upper_df = upper_columns(df, cols)
        expected_df = spark.createDataFrame([("ABC", "CEF", 1)], cols)
        assert_df_equality(upper_df, expected_df)


if __name__ == "__main__":
    # Run the tests
    result = UnitTest().execute_tests()
    print(result.to_string())

    # Raise an exception if any of the tests failed
    if result.test_results.num_failures > 0:
        raise Exception("Test failed.")
