class Party:
    def __init__(self):
        self.people = []

    def invite(self, name):
        self.people.append(name)

    def invited_name(self):
        return ', '.join(name for name in self.people)

    def pople_count(self):
        return len(self.people)


party = Party()

while True:
    name = input()
    if name == 'End':
        break
    party.invite(name)

print(f'Going: {party.invited_name()}')
print(f'Total: {party.pople_count()}')