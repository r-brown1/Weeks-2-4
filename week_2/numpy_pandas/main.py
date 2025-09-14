from student_analytics.src.data_loader import *
from week_2.numpy_pandas.student_analytics.src import data_loader
from week_2.numpy_pandas.student_analytics.src import merge_utils
from week_2.numpy_pandas.student_analytics.src import analysis


if __name__ == "__main__":
    # LOAD
    print("Loading student data...\n")
    student_grades = data_loader.load_student_data("./student_analytics/data/students.csv")
    student_scores = data_loader.load_student_data("./student_analytics/data/student_scores.csv")
    print("Student data loaded (rows, cols)\n", f"Student Grades: {student_grades.shape}\n Student Scores: {student_scores.shape}\n")

    # MERGE
    print("Merging student data...\n")
    merged_data = merge_utils.merge_student_data(student_grades, student_scores)
    print(f"Student data merged (rows, cols)\n Merged Student Data: {merged_data.shape}\n")
    print("MERGED STUDENT DATA\n", merged_data, "\n")


    # CLEAN
    print("Cleaning student data...")
    data_loader.clean_student_data(merged_data)
    print("Student data cleaned.\n")

    # ANALYZE
    print("Running data analysis...\n")

    print("STUDENT SCORES ANALYSIS")
    avg, med, std = analysis.student_scores_analysis(merged_data)
    print(f"Average Score: {avg}")
    print(f"Median Score: {med}")
    print(f"Standard Deviation: {std}\n")

    print("STUDENTS (Over 18)")
    print(analysis.list_students_gt_18(merged_data), "\n")

    print("STUDENTS (By Grade)")
    print(analysis.sort_by_grade(merged_data), "\n")

    # PLOT



