n = int(input())
word = input()

word_list = []
for i in range(0, n):
    sentence = input()
    word_list.append(sentence)


print(word_list)

for i in range(len(word_list) - 1, -1, -1):
    element = word_list[i]
    if word not in element:
        word_list.remove(element)
print(word_list)


