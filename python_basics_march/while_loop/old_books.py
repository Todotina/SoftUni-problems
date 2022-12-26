searched_book = input()
command = input()
count_books = 0

while command != "No More Books":
    if command == searched_book:
        print(f"You checked {count_books} books and found it.")
        break
    count_books += 1
    command = input()
if command == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {count_books} books.")
