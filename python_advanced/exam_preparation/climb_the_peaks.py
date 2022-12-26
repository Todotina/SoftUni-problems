from collections import deque

daily_portions = deque([int(x) for x in input().split(", ")])
daily_stamina = deque([int(x) for x in input().split(", ")])

peaks = [
    ('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70)
]
climbed_peaks = []
while daily_portions:
    daily_sum = daily_portions[-1] + daily_stamina[0]
    if daily_sum >= peaks[0][1]:
        daily_portions.pop()
        daily_stamina.popleft()
        climbed_peaks.append(peaks[0][0])
        del peaks[0]
    else:
        daily_portions.pop()
        daily_stamina.popleft()
    if len(climbed_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

if len(climbed_peaks) < 5:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if len(climbed_peaks) > 0:
    print("Conquered peaks:")
    for el in climbed_peaks:
        print(el)
