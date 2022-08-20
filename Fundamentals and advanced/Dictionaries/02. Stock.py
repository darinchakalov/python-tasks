stock = input().split(' ')
search_products = input().split(' ')

stock_dict = {}

for i in range(0, len(stock), 2):
    key = stock[i]
    val = int(stock[i + 1])
    stock_dict[key] = val


for item in search_products:
    if item in stock_dict.keys():
        print(f'We have {stock_dict[item]} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")