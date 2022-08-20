list_of_numbers = [int(i) for i in input().split(', ')]

boundry_value = 10

while len(list_of_numbers) > 0:
    result = [i for i in list_of_numbers if i <= boundry_value]
    list_of_numbers = [i for i in list_of_numbers if i not in result]
    print(f"Group of {boundry_value}'s: {result}")
    boundry_value += 10