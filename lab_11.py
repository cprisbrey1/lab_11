import csv

def write_grades():
    grades = open('grades.txt', 'w')

    SENTINAL = -99
    grade = None

    number_of_grades = 0
    while True:
        grade = int(input('please enter a grade, enter -99 to stop'))
        if grade != SENTINAL:
            if number_of_grades == 0:
                grades.write(f'{grade}')
            else:
                grades.write(f'\n{grade}')
            number_of_grades += 1

        elif grade == SENTINAL:
            break

    grades.close()

def average_grades():
    grades = open('grades.txt', 'r')
    grades_list = grades.readlines()
    grades_list = [int(g.replace('\n','')) for g in grades_list]
    print(grades_list)
    print(f'count: {len(grades_list)}')
    print(f'total: {sum(grades_list)}')
    print(f'average: {sum(grades_list)/len(grades_list)}')

def get_info():
    first_name = input('what is the students first name?  ')
    last_name = input('what is the students last name?  ')
    exam_1 = int(input('what was the students exam 1 grade? '))
    exam_2 = int(input('what was the students exam 2 grade? '))
    exam_3 = int(input('what was the studetns exam 3 grade? '))
    return([first_name, last_name, exam_1, exam_2, exam_3])

def write_csv(file, info):
    file.writerow({
        'first name': info[0], 
        'last name': info[1], 
        'exam 1 grade': info[2],
        'exam 2 grade': info[3],
        'exam 3 grade': info[4]})

def csv_grades():
    student_info = open('student_info.csv', 'w')
    fieldnames = ['first name', 'last name', 'exam 1 grade', 'exam 2 grade', 'exam 3 grade']
    writer = csv.DictWriter(student_info, fieldnames = fieldnames)
    writer.writeheader()
    while True:
        write_csv(writer, get_info())
        keep_going = input("enter more info?(y/n)")
        if keep_going == 'n':
            break
#write_grades()
#average_grades()
#csv_grades()
