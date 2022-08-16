import sys

current_year = int(input())

for year in range (current_year, sys.maxsize):

    if len(str(year)) == len(set(str(year))):
        print(year)
        break