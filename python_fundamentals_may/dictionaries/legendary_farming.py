legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
items = input().split(" ")
obtained = False
while True:
    for material in range(0, len(items), 2):
        quantity = int(items[material])
        item = items[material + 1].lower()
        if item in legendary_items:
            legendary_items[item] += quantity
        else:
            if item not in legendary_items:
                junk_items[item] = 0
            junk_items[item] += quantity
        if legendary_items["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary_items["shards"] -= 250
            obtained = True
        elif legendary_items["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary_items["fragments"] -= 250
            obtained = True
        elif legendary_items["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary_items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    items = input().split(" ")

for item, quantity in legendary_items.items():
    print(f"{item}: {quantity}")
for item, quantity in junk_items.items():
    print(f"{item}: {quantity}")