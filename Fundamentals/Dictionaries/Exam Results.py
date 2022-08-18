command = input()

BANNED = 'banned'

results = {}
submissions = {}

while command != 'exam finished':
    if BANNED in command:
        name, ban = command.split('-')
        del results[name]
    else:
        name, lang, score = command.split('-')
        if name in results.keys():
            if int(score) > results[name]:
                results[name] = int(score)
        else:
            results[name] = int(score)
        if lang in submissions.keys():
            submissions[lang] += 1
        else:
            submissions[lang] = 1

    command = input()


print('Results:')
for name in results:
    print(f'{name} | {results[name]}')
print('Submissions:')
for sub in submissions:
    print(f'{sub} - {submissions[sub]}')