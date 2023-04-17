#This one gave 87 points in the judge system
msg_received = {}
msg_sent = {}
capacity = int(input())

while True:
    line = input()
    if line == "Statistics":
        break

    command_args = line.split("=")
    command = command_args[0]

    if command == "Add":
        username = command_args[1]
        sent_msgs = int(command_args[2])
        received_msgs = int(command_args[3])

        if username not in msg_sent and username not in msg_received:
            msg_received[username] = received_msgs
            msg_sent[username] = sent_msgs

    elif command == "Message":
        sender = command_args[1]
        receiver = command_args[2]
        if sender in msg_sent and sender in msg_received and receiver in msg_sent and receiver in msg_received:
            msg_received[receiver] += 1
            msg_sent[sender] += 1

        if msg_sent[sender] + msg_received[sender] >= capacity:
            print(f"{sender} reached the capacity!")
            msg_received.pop(sender)
            msg_sent.pop(sender)
        if msg_sent[receiver] + msg_received[receiver] >= capacity:
            print(f"{receiver} reached the capacity!")
            msg_received.pop(receiver)
            msg_sent.pop(receiver)

    else:
        usrname = command_args[1]
        if usrname in msg_sent and usrname in msg_received:
            msg_received.pop(usrname)
            msg_sent.pop(usrname)
        if usrname == "All":
            msg_received.clear()
            msg_sent.clear()


print(f"Users count: {len(msg_received)}")
for name in msg_received.keys():
    print(f"{name} - {msg_received[name] + msg_sent[name]}")
