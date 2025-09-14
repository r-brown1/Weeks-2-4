import pandas as pd

def merge_student_data(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Merge student data from different files into a single dataframe and removing duplicate columns.
    :param df1: DataFrame with student data.
    :param df2: DataFrame with different student data.
    :return: DataFrame with merged student data.
    """
    df1.loc[df1["Age"] > 0, ["student_id"]] = df1.index
    df1["student_id"] = df1["student_id"].astype(int)

    merged_df = pd.merge(df1, df2, how="inner", on="student_id")
    merged_df.rename(columns={"Score_x": "Score"}, inplace=True)
    merged_df.drop(["Score_y"], axis=1, inplace=True)
    return merged_df