def kwargs_length(**kwargs):
    return len(kwargs.values())






dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
