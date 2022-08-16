import math

first = int(input())
second = int(input())
third = int(input())

combined = first + second + third

minutes = (math.floor(combined / 60))

seconds = (combined % 60)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
