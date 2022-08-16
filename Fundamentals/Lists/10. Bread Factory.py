input = input()

energy = 100
coins = 100

commants_list = (input.split('|'))
finished = True

for i in range(0, len(commants_list)):
    command, num = commants_list[i].split('-')
    num = int(num)
    if command == 'rest':
        missing_energy = 100 - energy
        if missing_energy >= (num):
            energy += num
            print(f'You gained {num} energy.')
        else:
            energy += missing_energy
            print(f'You gained {missing_energy} energy.')
        print(f'Current energy: {energy}.')
    elif command == 'order':
        energy -= 30
        if energy > 0:
            print(f'You earned {num} coins.')
            coins += num
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print('You had to rest!')
    else:
        if num <= coins:
            coins -= num
            print(f'You bought {command}.')
        else:
            print(f'Closed! Cannot afford {command}.')
            finished = False
            break

if finished:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')