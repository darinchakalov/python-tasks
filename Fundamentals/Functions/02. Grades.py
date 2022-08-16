grade = float(input())

def check_grade(n):
    if n < 3:
        print('Fail')
    elif n >=3 and n < 3.50:
        print('Poor')
    elif n >= 3.50 and n < 4.5:
        print('Good')
    elif n >= 4.5 and n < 5.50:
        print('Very Good')
    else:
        print('Excellent')

check_grade(grade)