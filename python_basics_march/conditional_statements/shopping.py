budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())
value_video_cards = video_cards * 250
value_processors = processors * (0.35 * value_video_cards)
value_ram = ram * (0.1 * value_video_cards)
discount = 0
if video_cards > processors:
    discount = 0.15 * (value_ram + value_processors + value_video_cards)
total_value = value_ram + value_processors + value_video_cards - discount
if total_value <= budget:
    print(f'You have {budget - total_value:.2f} leva left!')
elif total_value > budget:
    print(f'Not enough money! You need {abs(total_value - budget):.2f} leva more!')
