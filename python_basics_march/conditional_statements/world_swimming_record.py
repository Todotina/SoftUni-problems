from math import floor
world_record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())
delay = floor(distance_meters / 15) * 12.5

time_seconds = distance_meters * seconds_per_meter + delay
difference = abs(world_record_seconds - time_seconds)
if time_seconds < world_record_seconds:
    print(f'Yes, he succeeded! The new world record is {time_seconds:.2f} seconds.')
elif time_seconds >= world_record_seconds:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')

