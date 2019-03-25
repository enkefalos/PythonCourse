def compare_subjects_within_student(subj1_all_students :dict,
                                    subj2_all_students :dict):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    for key, val in subj1_all_students.items():
        if key != 'subject' and key in subj2_all_students:
            print(key, end = ' ')
            if max(val) > max(subj2_all_students[key]):
                print(subj1_all_students['subject'])
                continue
            
            print(subj2_all_students['subject'])




if __name__ == '__main__':
    # Question 3

    math_grades = {
        'subject': 'Math',
        'Zvi': (100, 98),
        'Omri': (68, 93),
        'Shira': (90, 90),
        'Rony': (85, 88) }

    history_grades = {
        'subject': 'History',
        'Zvi': (69, 73),
        'Omri': (88, 74),
        'Shira': (92, 87),
        'Rony': (92, 98) }
    
    print('Preffered subject per student')
    compare_subjects_within_student(math_grades, history_grades)
