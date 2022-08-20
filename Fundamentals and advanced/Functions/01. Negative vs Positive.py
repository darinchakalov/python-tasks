def read_input():
    return [int(x) for x in input().split(' ')]

def find_positive_nums(nums):
    return sum([num for num in nums if num >= 0])

def find_negative_nums(nums):
    return sum([num for num in nums if num < 0])

def print_result(positive, negative):
    print(negative)
    print(positive)
    if positive > abs(negative):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')


numbers = read_input()
positive_sum = find_positive_nums(numbers)
negative_sum = find_negative_nums(numbers)
print_result(positive_sum, negative_sum)