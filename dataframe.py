"""
A python module dataframe.py that reads the data in homework 2; and generates
a ValueError execption if the dataframe doesn't have the expected column names.
Also, ensures that the dataframe has at least 3 columns.
"""

import pandas as pd


def dataframe():
    """
    Function reads in the auto data, drops the NA values, and ensures that
    there are at least 3 columns.
    Also, it generates a ValueError execption if the dataframe doesn't have
    the expected column names.

    Inputs: None
    Outputs: The DataFrame which was read
    """
    auto_data = pd.read_csv("http://www-bcf.usc.edu/~gareth/ISL/Auto.csv",
                            na_values='?')
    auto_data = auto_data.dropna()

    if len(auto_data.columns) < 3:
        raise "The DataFrame has less than 3 columns."

    for col_name in ['mpg', 'cylinders', 'weight', 'year']:
        if col_name not in auto_data.columns:
            raise ValueError("DataFrame should have a column named '%s."
                             % col_name)
    return auto_data
