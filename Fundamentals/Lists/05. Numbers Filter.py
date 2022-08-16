n = int(input())

nums = []
command = ''
for i in range(0, n):
        num = int(input())
        nums.append(num)


command = input()

if command == 'even':
    print(list(filter(lambda c: c % 2 == 0, nums)))
elif command == 'odd':
    print(list(filter(lambda c: c % 2 != 0, nums)))
elif command == 'negative':
    print(list(filter(lambda c: c < 0, nums)))
elif command == 'positive':
    print(list(filter(lambda c: c >= 0, nums)))