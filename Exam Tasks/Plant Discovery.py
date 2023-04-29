num = int(input())
plants = {}
for i in range(num):
    command = input().split("<->")
    plant = command[0]
    rarity = int(command[1])
    if plant not in plants.keys():
        plants[plant] = []
        plants[plant].append(rarity)
    else:
        plants[plant] = []
        plants[plant].append(rarity)

while True:
    command = input()
    if command == "Exhibition":
        break
    current_command = command.split(": ")[0]
    second_part = command.split(": ")[1]
    if "Rate" in command:
        plant_to_be_rated = second_part.split(" - ")[0]
        rating_plant = int(second_part.split(" - ")[1])
        if plant_to_be_rated not in plants.keys():
            print("error")
        else:
            plants[plant_to_be_rated].append(rating_plant)
    elif "Update" in command:
        plant_tobe_updated = second_part.split(" - ")[0]
        if plant_tobe_updated not in plants.keys():
            print("error")
        else:
            new_rarity = int(second_part.split(" - ")[1])
            plants[plant_tobe_updated].pop(0)
            plants[plant_tobe_updated].insert(0, new_rarity)
    elif "Reset" in command:
        plant_to_be_reset = command.split(": ")[1]
        if plant_to_be_reset not in plants.keys():
            print("error")
        else:
            rarity_to_add_back = plants[plant_to_be_reset][0]
            plants[plant_to_be_reset].clear()
            plants[plant_to_be_reset].append(rarity_to_add_back)
            # plants[plant_to_be_reset].insert(1, 0)
    else:
        print("error")

for key, value in plants.items():
    item_to_amend = value[1:]
    remaining_part = value[0]
    if len(item_to_amend) > 1:
        total = sum(item_to_amend)
        new_num = total / len(item_to_amend)
        value.clear()
        value.append(remaining_part)
        value.append(new_num)
    if len(value) == 1:
        value.append(0)

print(f"Plants for the exhibition:")
plants = dict(sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1])))
for key, value in plants.items():
    print(f"- {key}; Rarity: {int(value[0])}; Rating: {value[1]:.2f}")