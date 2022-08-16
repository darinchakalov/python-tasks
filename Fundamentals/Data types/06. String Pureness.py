count = int(input())

for i in range(0, count):
    new_sting = input()

    if (',' in new_sting) or ('.' in new_sting) or ('_' in new_sting):
        print(f'{new_sting} is not pure!')
    else:
        print(f'{new_sting} is pure.')