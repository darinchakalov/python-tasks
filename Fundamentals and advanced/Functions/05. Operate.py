from functools import reduce

def operate(operator, *args):
    mapper = {
        "+": lambda x, y: x+y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    return reduce(mapper[operator], args)


print(operate("+", 3,4))