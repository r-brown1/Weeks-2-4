from data_toolkit.data import students
from data_toolkit.utils import info_utils
from data_toolkit.utils import hobby_utils

def run_general_report(data):
    print(info_utils.get_score_summary(data))
    print(info_utils.get_average_age(data))
    print(info_utils.filter_high_scores(data, 80))

def add_hobby_and_print_report(name, hobby, data = students.STUDENT_DATA):
    hobby_utils.add_hobby(name, hobby, data)
    print(data[0])

if __name__ == '__main__':
    run_general_report(students.STUDENT_DATA)
    add_hobby_and_print_report('Joe Feldman', "Jogging", students.STUDENT_DATA)
    # add_hobby_and_print_report('Joe Feldman', "Music", students.STUDENT_DATA)

