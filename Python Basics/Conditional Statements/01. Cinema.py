projection = input()
r = int(input())
c = int(input())

price = 0

if projection == 'Premiere':
    price = 12
elif projection == 'Normal':
    price = 7.5
else:
    price = 5

format_float = "{:.2f}".format(float(r * c * price))

print(f'{format_float} leva')
