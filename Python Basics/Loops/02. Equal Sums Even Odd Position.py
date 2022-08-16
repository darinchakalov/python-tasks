first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num+1):
    num = str(i)
    sum_odd = 0
    sum_even = 0
    for index, digit in enumerate(num):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    if sum_odd == sum_even:
        print(i, end=' ')