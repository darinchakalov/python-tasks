book_name = input()

count = 0

searched_book = ''
found = False

while (True):
    searched_book = input()

    if searched_book == book_name:
        found = True
        break

    if searched_book == "No More Books":
        break

    count += 1

if found :
    print(f'You checked {count} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {count} books.')



