hour = int(input())
minutes = int(input())
time = minutes + 15
actual_minutes = time % 60
actual_hour = 0
if time >= 60:
    actual_hour = hour + 1
else:
    actual_hour = hour
if actual_hour > 23:
    actual_hour = 0

if actual_minutes < 10:
    print(f'{actual_hour}:0{actual_minutes}')
else:
    print(f'{actual_hour}:{actual_minutes}')

