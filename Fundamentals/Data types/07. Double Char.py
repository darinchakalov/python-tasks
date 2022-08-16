command = input()

while command != 'End':
    if command != 'SoftUni':
        for index, char in enumerate(command):
            print(char, end='')
            if index == len(command) - 1:
                print(char)
            else:
                print(char, end='')

    command = input()