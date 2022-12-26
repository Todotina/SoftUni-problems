number_of_heroes = int(input())
heroes = {}

for hero in range(number_of_heroes):
    hero_info = input().split(" ")
    hero_name, hit_points, mana_points = hero_info[0], int(hero_info[1]), int(hero_info[2])
    if hero_name not in heroes:
        heroes[hero_name] = {}
        heroes[hero_name]['hp'] = hit_points
        heroes[hero_name]['mp'] = mana_points


def cast_spell(hero_name, mp_needed):
    if heroes[hero_name]['mp'] >= mp_needed:
        heroes[hero_name]['mp'] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mp']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(hero_name, damage):
    if heroes[hero_name]['hp'] > damage:
        heroes[hero_name]['hp'] -= damage
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del heroes[hero_name]


def recharge_hero(hero_name, amount):
    delta = 200 - heroes[hero_name]['mp']
    if delta < amount:
        heroes[hero_name]['mp'] = 200
        print(f"{hero_name} recharged for {delta} MP!")
    else:
        heroes[hero_name]['mp'] += amount
        print(f"{hero_name} recharged for {amount} MP!")


def heal_hero(hero_name, amount):
    delta = 100 - heroes[hero_name]['hp']
    if delta < amount:
        heroes[hero_name]['hp'] = 100
        print(f"{hero_name} healed for {delta} HP!")
    else:
        heroes[hero_name]['hp'] += amount
        print(f"{hero_name} healed for {amount} HP!")


command = input()

while command != "End":
    current_command = command.split(" - ")
    action, hero_name = current_command[0], current_command[1]
    if action == "CastSpell":
        mp_needed = int(current_command[2])
        spell_name = current_command[3]
        cast_spell(hero_name, mp_needed)
    elif action == "TakeDamage":
        damage = int(current_command[2])
        attacker = current_command[3]
        take_damage(hero_name, damage)
    elif action == "Recharge":
        amount = int(current_command[2])
        recharge_hero(hero_name, amount)
    elif action == "Heal":
        amount = int(current_command[2])
        heal_hero(hero_name, amount)
    command = input()

if command == "End":
    for hero_name in heroes:
        print(f"{hero_name} \n HP: {heroes[hero_name]['hp']} \n MP: {heroes[hero_name]['mp']}")
