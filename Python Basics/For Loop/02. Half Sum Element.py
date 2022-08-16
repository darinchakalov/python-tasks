import sys

n = int(input())

max_sum = 0
max_num = -sys.maxsize

for i in range(0, n):
    num = int(input())

    if num > max_num:
        max_num = num

    max_sum += num

if max_num == max_sum - max_num:
    print('Yes')
    print(f'Sum = {max_sum - max_num}')

else:
    print('No')
    print(f'Diff = {abs(max_num - (max_sum - max_num))}')
