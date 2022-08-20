from collections import deque

quantity = int(input())

people_list = deque()

command = input()

substring = 'refill'

while command != 'Start':
    people_list.append(command)
    command = input()

command = input()
while command != 'End':
    if substring in command:
        ref, num = command.split(' ')
        quantity += int(num)
    else:
        command = int(command)
        if quantity >= (command):
            print(f'{people_list.popleft()} got water')
            quantity -= (command)
        else:
            print(f'{people_list.popleft()} must wait')



    command = input()


print(f'{quantity} liters left')
