def find_it(seq):
    obj = {}
    for i in seq:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1

    for x in obj:
        if obj[x] % 2 != 0:
            return x


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_it([10]))
print(find_it([10, 10, 10]))
print(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]))
print(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]))