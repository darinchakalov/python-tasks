
def square_sum(numbers):
    result = 0
    for item in numbers:
        result += item ** 2
    return result


print(square_sum([1, 2]))
print(square_sum([0, 3, 4, 5]))
print(square_sum([]))
