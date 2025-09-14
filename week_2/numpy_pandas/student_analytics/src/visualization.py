import pandas as pd
import matplotlib.pyplot as plt
from data_loader import *
data = load_student_data('../data/students.csv')
dataf = pd.DataFrame(data)

def plot_histogram(df):
    # TODO - Learn how to use matplotlib in Pycharm
    """
    Plots histogram of student data
    :param df: DataFrame for student data
    :return: None -> Information displayed in separate window
    """
    return

print(plot_histogram(dataf))