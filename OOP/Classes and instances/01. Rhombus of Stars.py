size = int(input())


def print_row(size, start_count):
    for row in range(size - start_count):
        print(' ', end="")
    for row in range(1, start_count):
        print("*", end=" ")
    print('*')


for star_count in range(1, size):
    print_row(size, star_count)
for star_count in range(size, 0, -1):
    print_row(size, star_count)
