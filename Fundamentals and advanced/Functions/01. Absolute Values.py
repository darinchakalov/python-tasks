input = input()

list = (input.split())
new_list = []
for item in list:
   new_list.append(abs(float(item)))

print(new_list)