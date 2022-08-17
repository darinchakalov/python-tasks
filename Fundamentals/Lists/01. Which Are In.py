first_list = input().split(', ')
second_list = input().split(', ')

print([s for s in first_list if any(s in i for i in second_list)])