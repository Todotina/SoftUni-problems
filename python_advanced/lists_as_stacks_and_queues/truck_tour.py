from collections import deque

number_petrol_pumps = int(input())
tank = 0
pump_index = ''
for index in range(number_petrol_pumps):
    current_data = input().split()
    petrol = int(current_data[0])
    distance = int(current_data[1])
    if petrol >= distance:
        tank += petrol
        pump_index = index
        break
    else:
        continue
print(pump_index)
