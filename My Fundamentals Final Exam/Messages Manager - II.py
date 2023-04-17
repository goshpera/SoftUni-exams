limit = int(input())

command = input()

users = []
send_and_received = []
users_dict = {}

while True:
    if command == "Statistics":
        break

    commands = command.split('=')

    if commands[0] == "Add":
        if commands[0] not in users:
            users.append(commands[1])
            send = int(commands[2])
            received = int(commands[3])
            sum_send_received = send + received
            send_and_received.append(sum_send_received)

    if commands[0] == "Message":
        if commands[1] and commands[2] in users:
            count1 = 0
            count2 = 0
            for x in users:
                if commands[1] == x:
                    send_and_received[count1] += 1
                    if send_and_received[count1] >= limit:
                        send_and_received.pop(count1)
                        print(f"{users[count1]} reached the capacity!")
                        users.pop(count1)
                else:
                    count1 += 1
            count1 = 0
            for sec in users:
                if commands[2] == sec:
                    send_and_received[count2] += 1
                    if send_and_received[count2] >= limit:
                        send_and_received.pop(count2)
                        print(f"{users[count2]} reached the capacity!")
                        users.pop(count2)
                else:
                    count2 += 1
            count2 = 0

    if commands[0] == "Empty":
        if commands[1] == "All":
            users.clear()
            send_and_received.clear()
        if commands[1] in users:
            user_count = 0
            for u in users:
                if commands[1] == u:
                    users.pop(user_count)
                    send_and_received.pop(user_count)
                else:
                    user_count += 1
    command = input()

print(f"Users count: {len(users)}")
for key, val in zip(users, send_and_received):
    print(f"{key} - {val}")
