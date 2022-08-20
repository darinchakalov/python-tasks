def multiply(*args):
    sum = 1

    for num in args:
        sum *= int(num)

    return sum



multiply(1, 4, 5)