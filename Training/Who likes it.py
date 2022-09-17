def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 3 or len(names) == 2:
        last_name = names.pop()
        return f'{", ".join(names)} and {last_name} like this'
    else:
        first_name = names.pop(0)
        second_name = names.pop(0)
        return f"{first_name}, {second_name} and {len(names)} others like this"


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max", 'Peter']))
