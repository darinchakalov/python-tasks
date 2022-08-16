command = input()

prime_sum = 0
non_prime_sum = 0

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

while command != 'stop':
    if (command != 'stop'):
        num = int(command)

    if num < 0:
        print('Number is negative.')
    else:
        if is_prime(num):
            prime_sum += num
        else:
            non_prime_sum += num
    command = input()


print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')