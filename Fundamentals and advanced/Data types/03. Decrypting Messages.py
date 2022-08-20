key = int(input())
n = int(input())

result = ''
for i in range(0, n):
    new_char = input()
    result += (chr(ord(new_char)+key))

print(result)