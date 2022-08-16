num = int(input())

current = 1
inner_loop_break = False

for row in range(1, num + 1):
    for col in range(1, row + 1):
        if current > num:
            inner_loop_break = True
            break

        print(str(current) + ' ', end='')
        current += 1

    if inner_loop_break:
        break
    print()