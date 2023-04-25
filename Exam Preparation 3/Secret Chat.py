text = input()

while True:
    line = input()
    if line == "Reveal":
        break

    command_args = line.split(":|:")
    command = command_args[0]

    if command == "InsertSpace":
        idx = int(command_args[1])
        text = text[:idx] + " " + text[idx:]
        print(text)

    elif command == "Reverse":
        substr = command_args[1]
        if substr in text:
            text = text.replace(substr, "", 1)
            text += substr[::-1]
            print(text)
        else:
            print("error")

    elif command == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]
        if substring in text:
            text = text.replace(substring, replacement)
            print(text)

print(f"You have a new text message: {text}")
