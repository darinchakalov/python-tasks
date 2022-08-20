def rectangle(*args):
    for arg in args:
        if isinstance(arg, str):
            return 'Enter valid values!'
    return f'Rectangle area: {args[0] * args[1]}\nRectangle perimeter: {args[0] * 2 + args[1] * 2}'



print(rectangle(2, 10))
print(rectangle('2', 10))