percentage = int(input())

perc = '%'
dot = '.'

def loading_bar(per):
    per_string = perc * int(per/10)
    dot_string = dot * int((100 - per) / 10)
    if per == 100:
        print(f'100% Complete!')
        print(f'[{per_string}]')
    else:
        print(f'{per}% [{per_string}{dot_string}]')
        print('Still loading...')

loading_bar(percentage)