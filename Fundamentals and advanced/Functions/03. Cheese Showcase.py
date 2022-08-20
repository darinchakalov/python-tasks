def sorting_cheeses(**kwargs):
    result = {}

    for key, value in kwargs.items():
        result[key] = sorted(value, key=None, reverse=True)

    string_result = ''

    for key in sorted(result):
        string_result += f'{key}\n'
        for value in result[key]:
            string_result += f'{value}\n'
    return  string_result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
