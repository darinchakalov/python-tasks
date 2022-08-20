def even_odd_filter(**kwargs):
    result = {}
    for key in kwargs.keys():
        if key == 'even':
            result[key] = [i for i in kwargs[key] if i % 2 == 0]
        else:
            result[key] = [i for i in kwargs[key] if i % 2 != 0]
    return  result

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
