dollar_price_processor = float(input())
dollar_price_video_card = float(input())
dollar_price_per_ram = float(input())
count_ram = int(input())
percent_discount = float(input())
total_price_usd = (dollar_price_per_ram * count_ram) + (1 - percent_discount) * (dollar_price_processor + dollar_price_video_card)
total_price_bgn = total_price_usd * 1.57
print(f"Money needed - {total_price_bgn:.2f} leva.")