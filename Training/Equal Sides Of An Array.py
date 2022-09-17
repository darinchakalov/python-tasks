def find_even_index(arr):
    found_index = -1

    for idx, num in enumerate(arr):
        if sum(arr[:idx]) == sum(arr[idx+1:]):
            found_index = idx
            break

    return found_index


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
print(find_even_index([1, 100, 50, -51, 1, 1]))
print(find_even_index([1, 2, 3, 4, 5, 6]))
print(find_even_index([20, 10, 30, 10, 10, 15, 35]))
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))
print(find_even_index([10, -80, 10, 10, 15, 35, 20]))
print(find_even_index([0, 0, 0, 0, 0]))
print(find_even_index([-1, -2, -3, -4, -3, -2, -1]))
