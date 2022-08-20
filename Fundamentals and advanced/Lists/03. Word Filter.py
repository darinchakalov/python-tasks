input_words = input().split(' ')

try_filter = [x for x in input_words if len(x) % 2 == 0]
filtered_word_list = list(filter(lambda x: len(x) % 2 == 0, input_words))

print('\n'.join(try_filter))