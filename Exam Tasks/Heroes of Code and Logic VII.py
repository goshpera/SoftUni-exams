num = int(input())
hp_by_hero = {}
mp_by_hero = {}

for i in range(num):
    heroes = input().split()
    hero = heroes[0]
    hp = min(int(heroes[1]), 100)
    mp = min(int(heroes[2]), 200)
    hp_by_hero[hero] = hp
    mp_by_hero[hero] = mp

while True:
    line = input()
    if line == "End":
        break

    command_args = line.split(" - ")
    command = command_args[0]
    hero_name = command_args[1]

    if command == "CastSpell":
        mp_needed = int(command_args[2])
        spell_name = command_args[3]
        if mp_by_hero[hero_name] >= mp_needed:
            mp_by_hero[hero_name] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {mp_by_hero[hero_name]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(command_args[2])
        attacker = command_args[3]
        hp_by_hero[hero_name] -= damage
        if hp_by_hero[hero_name] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hp_by_hero[hero_name]} HP left!")
        else:
            hp_by_hero.pop(hero_name)
            mp_by_hero.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == "Recharge":
        amount_mp = int(command_args[2])
        print(f"{hero_name} recharged for {max((mp_by_hero[hero_name] - amount_mp),0)} MP!")
        mp_by_hero[hero_name] = min((mp_by_hero[hero_name] + amount_mp), 200)

    else:
        amount_hp = int(command_args[2])
        print(f"{hero_name} healed for {max((mp_by_hero[hero_name] - amount_hp), 0)} HP!")
        hp_by_hero[hero_name] = min((mp_by_hero[hero_name] + amount_hp), 100)

for name in hp_by_hero.keys():
    hp_left = hp_by_hero[name]
    mp_left = mp_by_hero[name]
    print(f"{name}\n  HP: {hp_left}\n  MP: {mp_left}")
