def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


print(to_camel_case(''))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))