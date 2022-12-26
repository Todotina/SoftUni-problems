number_of_rooms = int(input())
total_free_chairs = 0
for room in range(1, number_of_rooms + 1):
    current_room = input().split(" ")
    chairs = len(current_room[0])
    visitors = int(current_room[1])
    needed_chairs = visitors - chairs
    free_chairs = chairs - visitors
    if visitors > chairs:
        print(f"{needed_chairs} more chairs needed in room {room}")
    total_free_chairs += free_chairs
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")