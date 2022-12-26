length = int(input())
width = int(input())
height = int(input())
percent = float(input())
# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.
total_volume = length * width * height * 0.001
water_volume = total_volume * (1-percent/100)
print(water_volume)