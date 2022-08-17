input_list = list(map(lambda x: int(x), input().split(', ')))

positive_list = (x for x in input_list if x >= 0)
negative_list = [x for x in input_list if x < 0]
even_List = [x for x in input_list if x % 2 == 0]
odd_List = [x for x in input_list if x % 2 != 0]

print(f'Positive: {", ".join(list(map(lambda x: str(x), positive_list)))}')
print(f'Negative: {", ".join(list(map(lambda x: str(x), negative_list)))}')
print(f'Even: {", ".join(list(map(lambda x: str(x), even_List)))}')
print(f'Odd: {", ".join(list(map(lambda x: str(x), odd_List)))}')