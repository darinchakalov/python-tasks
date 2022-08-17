class Email:
    def __init__(self, sender, receiver, content, is_send = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = is_send


    def send(self):
        self.is_send = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}'



emails = []

while True:
    command = input()
    if command == 'Stop':
        break

    sender, receiver, content = command.split(' ')
    emails.append(Email(sender,receiver, content))


indices = [int(x) for x in input().split(', ')]

for index in indices:
    emails[index].send()

for mail in emails:
    print(mail.get_info())


