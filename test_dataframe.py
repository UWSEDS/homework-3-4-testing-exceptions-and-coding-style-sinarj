"""
A python file test_dataframe.py that has unit tests for dataframe.py
"""

from dataframe import dataframe


def test_expected_columns():
    """
    Checks if the dataframe has the expected columns or not
    """
    data = dataframe()
    test_res = True
    for col_name in ['mpg', 'cylinders', 'weight', 'year']:
        if col_name not in data.columns:
            test_res = False
            break
    assert test_res


def test_expected_columns_types():
    """
    Checks if all the columns are of the expected type
    """
    data = dataframe()
    assert(data.dtypes.mpg == float and data.dtypes.cylinders == int and
           data.dtypes.weight == int and data.dtypes.year == int)


def test_no_nan_values():
    """
    Checks to ensure that the dataframe has no nan values
    """
    data = dataframe()
    assert not data.isnull().sum().sum()


def test_expected_atleast_one_row():
    """
    Checks if the dataframe has at least one row
    """
    data = dataframe()
    assert len(data.index) >= 1
