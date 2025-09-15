import pandas as pd
import numpy as np
from typing import List

def one_hot_encode(df: pd.DataFrame, columns: List) -> pd.DataFrame:
    """
    Uses one-hot encoding for list of columns
    :param df: DataFrame
    :param columns: List of column names
    :return: DataFrame with one hot encoded columns
    """

    new_df = df
    try:
        new_df = pd.get_dummies(df, columns=columns)
        print("One-hot encoded columns added successfully\n")
    except ValueError:
        print("One-hot encoding failed")

    return new_df
        

def drop_income_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes income outliers from DataFrame
    :param df: DataFrame
    :return: None
    """
    new_df = df.copy()
    try:
        income_outliers = df[np.abs(df["income"] - df["income"].mean()) > 3 * df["income"].std()]
        new_df.drop(income_outliers.index, inplace=True)
        print("Income outliers successfully removed\n")
    except ValueError:
        print("Failed to drop income outliers")

    return new_df
        
        
def handle_salary_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates salary outlier report
    :param df: DataFrame
    :return: DataFrame with salary outliers
    """

    q1 = df["salary"].quantile(0.25)
    q3 = df["salary"].quantile(0.75)
    iqr = q3 - q1

    outliers = df
    try:
        outliers = df[(df["salary"] > (q3 + iqr * 1.5)) | (df["salary"] < (q1 - iqr * 1.5))]
        print("SALARY OUTLIER REPORT\n")
    except ValueError:
        print("Failed to handle salary outliers")

    return outliers

def flag_expense_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Flags expense outliers in new column
    :param df: DataFrame
    :return: DataFrame with expense outliers flagged
    """
    try:
        df["expenses_outlier"] = df["expenses"] > 1500
        print("Successfully added expenses outlier column to DataFrame\n")
    except ValueError:
        print("Failed to flag expense outliers")

    return df
