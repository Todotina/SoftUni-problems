from math import floor
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
exam_time_minutes = exam_hour * 60 + exam_minute
arrival_time_minutes = arrival_hour * 60 + arrival_minute
difference = exam_time_minutes - arrival_time_minutes
difference_hours = floor(abs(difference / 60))
difference_minutes = abs(difference % 60)

if difference > 30:
    print("Early")
    if difference_hours >= 1:
        if difference_minutes < 10:
            print(f"{difference_hours}:0{difference_minutes} hours before the start")
        else:
            print(f"{difference_hours}:{difference_minutes} hours before the start")
    else:
        print(f"{abs(difference)} minutes before the start")
elif difference == 0:
    print("On Time")
elif difference > 0:
    print("On Time")
    print(f"{abs(difference)} minutes before the start")
else:
    print("Late")
    if difference_hours >= 1:
        if difference_minutes < 10:
            print(f"{difference_hours}:0{difference_minutes} hours after the start")
        else:
            print(f"{difference_hours}:{difference_minutes} hours after the start")
    else:
        print(f"{abs(difference)} minutes after the start")
