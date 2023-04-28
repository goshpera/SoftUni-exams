def is_valid_idx(idx):
    return 0 <= idx <= len(key)


key = input()

while True:
    line = input()
    if line == "Generate":
        break

    command_args = line.split(">>>")
    command = command_args[0]

    if command == "Contains":
        substring = command_args[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        if command_args[1] == "Upper":
            start_idx = int(command_args[2])
            end_idx = int(command_args[3])
            if is_valid_idx(start_idx) and is_valid_idx(end_idx):
                key = key[:start_idx] + key[start_idx:end_idx].upper() + key[end_idx:]
                print(key)
        elif command_args[1] == "Lower":
            start_idx = int(command_args[2])
            end_idx = int(command_args[3])
            if is_valid_idx(start_idx) and is_valid_idx(end_idx):
                key = key[:start_idx] + key[start_idx:end_idx].lower() + key[end_idx:]
                print(key)

    else:
        startIdx = int(command_args[1])
        endIdx = int(command_args[2])
        if is_valid_idx(startIdx) and is_valid_idx(endIdx):
            key = key[:startIdx] + key[endIdx:]
            print(key)

print(f"Your activation key is: {key}")
