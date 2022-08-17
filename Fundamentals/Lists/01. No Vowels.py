word = input()

result = ''

for letter in list(word):
    if letter != 'a' and letter != 'o' and letter != 'u' and letter != 'e' and letter != 'i':
        result += letter

print(result)
