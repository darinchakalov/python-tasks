command = input()

stock = {}

while command != 'statistics':
    product, quantity = command.split(': ')
    quantity = int(quantity)
    if product in stock.keys():
        stock[product] += quantity
    else:
        stock[product] = quantity


    command = input()

print('Products in stock:')

total_quantity = 0

for product in stock:
    print(f'- {product}: {stock[product]}')
    total_quantity += int(stock[product])
print(f'Total Products: {len(stock.keys())}')
print(f'Total Quantity: {total_quantity}')