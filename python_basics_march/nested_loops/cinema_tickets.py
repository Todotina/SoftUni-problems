movie_name = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
while movie_name != "Finish":
    capacity = int(input())
    command = input()
    sold_tickets_current_movie = 0
    while command != "End":
        ticket_type = command
        sold_tickets_current_movie += 1
        total_tickets += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        else:
            standard_tickets += 1
        if sold_tickets_current_movie == capacity:
            break
        command = input()
    print(f"{movie_name} - {sold_tickets_current_movie / capacity * 100:.2f}% full.")
    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets/total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets/total_tickets*100:.2f}% standard tickets.")
print(f"{kids_tickets/total_tickets*100:.2f}% kids tickets.")