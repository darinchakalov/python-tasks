stock = input().split(' ')

stock_dict = {}

for i in range(0, len(stock), 2):
    key = stock[i]
    val = int(stock[i + 1])
    stock_dict[key] = val

print(stock_dict)