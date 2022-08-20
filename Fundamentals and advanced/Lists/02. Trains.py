n= int(input())

new_list = [0] * n

line = input()

while line != 'End':
    commands = line.split()
    if len(commands) == 3:
        command = commands[0]
        num1 = commands[1]
        num2 = commands[2]
    else:
        command = commands[0]
        num1 = commands[1]
    if command == 'add':
        new_list[n - 1] += int(num1)
    elif command == 'insert':
        new_list[int(num1)] += int(num2)
    elif command =='leave':
        new_list[int(num1)] -= int(num2)

    line = input()

print(new_list)
