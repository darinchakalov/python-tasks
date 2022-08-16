number_grades = int(input())

command = input()
count_all_grades = 0
count_poor_grades = 0
all_grades = 0
breaked = False
last_task = ''

while (command != 'Enough'):
    grade = int(input())
    all_grades += grade
    count_all_grades += 1
    if grade <= 4:
        count_poor_grades += 1

    if count_poor_grades == number_grades:
        breaked = True
        break
    command = input()
    if command != 'Enough':
        last_task = command


if breaked:
    print(f'You need a break, {count_poor_grades} poor grades.')
else:
    print(f'Average score: {(all_grades / count_all_grades):.2f}')
    print(f'Number of problems: {count_all_grades}')
    print(f'Last problem: {last_task}')

