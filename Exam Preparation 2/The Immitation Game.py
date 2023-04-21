def is_valid_idx(idx, seq):
    return 0 <= idx <= len(seq)


text = input()

while True:
    line = input()
    if line == "Decode":
        break

    command_args = line.split("|")
    command = command_args[0]

    if command == "Move":
        num_letters = int(command_args[1])
        if is_valid_idx(num_letters, text):
            text = text[num_letters:] + text[:num_letters]

    elif command == "Insert":
        index = int(command_args[1])
        value = command_args[2]
        if is_valid_idx(index, text):
            text = text[:index] + value + text[index:]

    elif command == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]
        if substring in text:
            text = text.replace(substring, replacement)

print(f"The decrypted message is: {text}")
