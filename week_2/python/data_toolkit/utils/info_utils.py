def get_average_age(student_list):
    cumulative_age = 0
    for student in student_list:
        cumulative_age += student['age']

    # Return type float
    return cumulative_age/len(student_list)

def get_score_summary(student_list):
    summary = { "min": 0, "max": 0, "avg": 0 }
    cumulative_score = 0
    for student in student_list:
        if student['score'] <= summary['min']:
            summary['min'] = student['score']

        if student['score'] >= summary['max']:
            summary['max'] = student['score']

        cumulative_score += student['score']

    summary['avg'] = int(cumulative_score)/len(student_list)

    # Return type dict with keys {min, max, avg}
    return summary

def filter_high_scores(student_dict, threshold=70):
    # NOTE - current value accessed before iteration is defined
    student_names = [student['name'] for student in student_dict if student['score'] >= threshold]


    # Returns type list of names
    return student_names