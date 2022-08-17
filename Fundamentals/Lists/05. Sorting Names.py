input = input().split(', ')

print(sorted(input, key=lambda x: (-len(x), x)))

