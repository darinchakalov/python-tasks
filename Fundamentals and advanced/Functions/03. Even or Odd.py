def even_odd(*args):
    nums_list = list(args)
    command =  nums_list.pop()
    if command == 'even':
        return [i for i in nums_list if i % 2 == 0]
    else:
        return [i for i in nums_list if i % 2 != 0]



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
