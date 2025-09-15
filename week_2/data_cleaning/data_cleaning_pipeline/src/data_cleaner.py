import pandas as pd
from typing import List

def get_df_from_csv(path: str) -> pd.DataFrame:
    """
    Get df from csv and create DataFrame
    :param path: path to csv file
    :return: DataFrame with raw data
    """

    df = pd.DataFrame()
    try:
        df = pd.DataFrame(pd.read_csv(path))
        print("Successfully read df from csv\n")
    except FileNotFoundError:
        print("File not found")

    return df


def generate_missing_values_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    :param df: DataFrame with missing values
    :return: DataFrame listing number of missing values by column
    """
    missing_values = pd.DataFrame(df.isna().sum())
    missing_values.rename(columns={missing_values.columns[0]: "Count"}, inplace=True)
    print("MISSING VALUES REPORT\n")
    return missing_values


def handle_missing_values(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    takes a list of columns and handles missing values

    RULES
    Age - replace with avg age
    Status - replace with 'Unknown'
    Other Missing Columns: remove from dataset

    :param df: DataFrame with missing values
    :param columns: list of column names
    :return: DataFrame with no missing values
    """
    try:
        for col in columns:
            if col == "age":
                df = df.fillna({col: df[col].mean()})
            elif col == "status":
                df = df.fillna({col: "Unknown"})
        df = df.dropna()
    except KeyError:
        print("FAILED: Key not found")

    return df

def standardize_string_values(df: pd.DataFrame, columns: List['str']) -> pd.DataFrame:
    """
    Standardizes list of columns with str values

    RULES
    Gender - replace with 'Male' or 'Female'
    Experience - remove 'years' and convert numeric value to int type
    Date - convert to datetime type
    Convert all other string columns to lowercase and removes whitespace
    :param df: DataFrame
    :param columns: list of column names (string types)
    :return: DataFrame with standardized strings
    """

    try:
        for col in columns:
            if col != "date":
                df[col] = df[col].str.strip()
                df[col] = df[col].str.lower()

            if col == "gender":
                df[col] = df[col].replace(
                    {'M': 'Male',
                     'm': 'Male',
                     'male': 'Male',
                     'MALE': 'Male',
                     'F': 'Female',
                     'f': 'Female',
                     'female': 'Female',
                     'FEMALE': 'Female',
                     })
            elif col == "experience":
                df[col] = df[col].str[0].astype(int)
            elif col == "date":
                df[col] = pd.to_datetime(df[col])
            print(f"Successfully standardized {col} values\n")

    except TypeError:
        print("FAILED: All columns in list must contain only string values\n")

    return df


def standardize_num_values(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Standardizes list of columns with int or float values

    RULES
    Price, Height - round value (2 decimal places)
    Age - convert to int type
    Sales - replace negative values with 0
    :param df: DataFrame
    :param columns: list of column names (numeric types)
    :return: DataFrame with standardized numeric values
    """
    
    try:
        for col in columns:
            if col == "price" or col == "height":
                df[col] = round(df[col].astype(float), 2)
            elif col == "age":
                df[col] = round(df[col].astype(int))
            elif col == "sales":
                df.loc[df[col] < 0, col] = 0
        print("Successfully standardized numeric values\n")
    except TypeError:
        print("All columns in list must contain integer values\n")

    return df


def min_max_normalize(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Normalize columns with numeric values using min/max scaling
    :param df: DataFrame 
    :param col: column name
    :return: DataFrame with normalized values
    """

    normalized_df = df

    try:
        normalized_df = df[f"normalized_{col}"] = round((df[col] - (df[col].min())) / (df[col].max() - df[col].min()), 2)
    except TypeError:
        print("Column must contain numeric values")

    return normalized_df