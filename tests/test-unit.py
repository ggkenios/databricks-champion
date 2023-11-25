# Databricks notebook source
from runtime.nutterfixture import NutterFixture
from chispa import assert_df_equality

from my_package import (
    generate_data1,
    generate_data2,
    spark,
    upper_columns,
)


class TestPercentRunFixture(NutterFixture):
    def __init__(self):
        self.code2_table_name = "my_data"
        self.code1_view_name = "my_cool_data"
        self.code1_num_entries = 100
        NutterFixture.__init__(self)

    def run_code1_percent_run(self):
        generate_data1(
            spark=spark,
            n=self.code1_num_entries,
            name=self.code1_view_name
        )

    def assertion_code1_percent_run(self):
        df = spark.read.table(self.code1_view_name)
        assert(df.count() == self.code1_num_entries)

    def run_code2_percent_run(self):
        generate_data2(table_name = self.code2_table_name)

    def assertion_code2_percent_run(self):
        some_tbl = spark.sql(f'SELECT COUNT(*) AS total FROM {self.code2_table_name}')
        first_row = some_tbl.first()
        assert (first_row[0] == 10)

    def after_code2_percent_run(self):
        spark.sql(f"drop table {self.code2_table_name}")

    def assertion_upper_columns_percent_run(self):
        cols = ["col1", "col2", "col3"]
        df = spark.createDataFrame([("abc", "cef", 1)], cols)
        upper_df = upper_columns(df, cols)
        expected_df = spark.createDataFrame([("ABC", "CEF", 1)], cols)
        assert_df_equality(upper_df, expected_df)


if __name__ == "__main__":
    # Run the tests
    result = TestPercentRunFixture().execute_tests()
    print(result.to_string())

    # Raise an exception if any of the tests failed
    if result.test_results.num_failures > 0:
        raise Exception("Test failed")
