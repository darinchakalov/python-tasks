operator = input()
n1 = int(input())
n2 = int(input())

def calculator(operator, n1, n2):
    if operator == 'multiply':
        return n1 * n2
    elif operator == 'divide':
        return  n1 / n2
    elif operator == 'add':
        return  n1 + n2
    elif operator == 'subtract':
        return  n1 - n2

print(int(calculator(operator, n1, n2)))
