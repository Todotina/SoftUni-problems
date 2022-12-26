class Party:

    def __init__(self):
        self.people = []


party = Party()
command = input()
total_people_going = 0
while command != "End":
    party.people.append(command)
    total_people_going += 1
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {total_people_going}")