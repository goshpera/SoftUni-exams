dict_pirates = {}
while True:
    input_first_line = input().split("||")

    if input_first_line[0] == "Sail":
        break

    city = input_first_line[0]
    if city in dict_pirates:
        population = input_first_line[1]
        gold = input_first_line[2]

        dict_pirates[city][0].append(population)
        popul = str(sum([int(x) for x in dict_pirates[city][0]]))
        dict_pirates[city][0] = [popul]

        # Gold calculations
        dict_pirates[city][1].append(gold)
        golddd = str(sum([int(z) for z in dict_pirates[city][1]]))
        dict_pirates[city][1] = [golddd]
    else:
        population = input_first_line[1]
        gold = input_first_line[2]
        dict_pirates[city] = [[population], [gold]]

while True:
    commands = input().split("=>")

    