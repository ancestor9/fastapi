homework_assignment_grade = {'homework1' : 100,
                             'homework2' : 90,
                             'homework3' : 70}

def calculate_homework(homework_assignment_arg):
    sum_of_grades =0
    for homework in homework_assignment_arg.values():
        sum_of_grades += homework
        
    final_grade = round(sum_of_grades/len(homework_assignment_arg))
    print(final_grade)
    
calculate_homework(homework_assignment_grade)