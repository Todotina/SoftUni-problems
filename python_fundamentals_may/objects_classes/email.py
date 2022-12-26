class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


message = input()
list_with_messages = []
while message != "Stop":
    message_list = [word for word in message.split(" ")]
    sender = message_list[0]
    receiver = message_list[1]
    content = message_list[2]
    email = Email(sender, receiver, content)
    list_with_messages.append(email)
    message = input()

if message == "Stop":
    send_emails = [int(number) for number in input().split(", ")]

for number in send_emails:
    list_with_messages[number].send()

for email in list_with_messages:
    print(email.get_info())