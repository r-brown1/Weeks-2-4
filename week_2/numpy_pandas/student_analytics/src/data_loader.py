import pandas as pd

def load_student_data(filename: str) -> pd.DataFrame:
    """
    Loads data from csv and creates a pandas DataFrame
    :param filename: string name of the csv file path
    :return: Dataframe for student data
    """
    student_data = pd.read_csv(filename)
    return pd.DataFrame(student_data)

def clean_student_data(df: pd.DataFrame) -> None:
    """
    Fill missing scores with avg and removes rows with NaN values
    :param df: DataFrame for student data
    :return: None -> DataFrame modified in place
    """
    df.fillna({"Score": df["Score"].mean()}, inplace=True)
    df.dropna(axis=0, how="any", subset=["Grade"], inplace=True)
    return




# print(load_student_data('../data/students.csv'))
