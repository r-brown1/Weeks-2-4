import pandas as pd
from typing import List

def sort_by_grade(df: pd.DataFrame) -> pd.DataFrame:
    """
    :param df: DataFrame for student data
    :return: DataFrame sorted by grade (high to low)
    """
    return df.sort_values(by=['Grade'], ascending=True)

def student_scores_analysis(df: pd.DataFrame) -> List[float]:
    """
    Prints average student score, median score, and standard deviation
    :param df: DataFrame for student data
    :return: None -> Information displayed in terminal
    """
    avg = round(df['Score'].mean(), 2)
    median = round(df['Score'].median(), 2)
    std = round(df['Score'].std(ddof=0), 2)
    return [avg, median, std]

def list_students_gt_18(df: pd.DataFrame) -> pd.DataFrame:
    """
    :param df: DataFrame for student data
    :return: DataFrame filtered by age (age > 18)
    """
    return df[df['Age'] > 18]

