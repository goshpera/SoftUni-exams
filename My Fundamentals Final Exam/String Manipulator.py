text = input()

while True:
    line = input()
    if line == "End":
        break

    command_args = line.split()
    command = command_args[0]

    if command == "Translate":
        old_char = command_args[1]
        replacement = command_args[2]
        if old_char in text:
            text = text.replace(old_char, replacement)
            print(text)
        else:
            print(text)

    elif command == "Includes":
        substring = command_args[1]

        if substring in text:
            print(True)
        else:
            print(False)

    elif command == "Start":
        sbstring = command_args[1]
        if text.startswith(sbstring):
            print(True)
        else:
            print(False)

    elif command == "Lowercase":
        text = text.lower()
        print(text)

    elif command == "FindIndex":
        searched_char = command_args[1]
        if searched_char in text:
            searched_idx = text.rfind(searched_char)
            print(searched_idx)
        else:
            continue

    else:
        start_idx = int(command_args[1])
        count = int(command_args[2])
        if start_idx < len(text) and count < len(text):
            text = text[0: start_idx] + text[start_idx + count:]
            print(text)
        else:
            continue
