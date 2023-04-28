num_of_pieces = int(input())
composer_of_piece = {}
key_of_piece = {}

for i in range(num_of_pieces):
    pieces = input().split("|")
    piece = pieces[0]
    composer = pieces[1]
    key = pieces[2]
    composer_of_piece[piece] = composer
    key_of_piece[piece] = key

while True:
    line = input()
    if line == "Stop":
        break

    command_args = line.split("|")
    command = command_args[0]
    piecee = command_args[1]

    if command == "Add":
        composerr = command_args[2]
        keyy = command_args[3]

        if piecee not in composer_of_piece and piecee not in key_of_piece:
            composer_of_piece[piecee] = composerr
            key_of_piece[piecee] = keyy
            print(f"{piecee} by {composerr} in {keyy} added to the collection!")
        else:
            print(f"{piecee} is already in the collection!")

    elif command == "Remove":
        if piecee in composer_of_piece and piecee in key_of_piece:
            composer_of_piece.pop(piecee)
            key_of_piece.pop(piecee)
            print(f"Successfully removed {piecee}!")
        else:
            print(f"Invalid operation! {piecee} does not exist in the collection.")

    else:
        new_key = command_args[2]
        if piecee in key_of_piece:
            key_of_piece[piecee] = new_key
            print(f"Changed the key of {piecee} to {new_key}!")
        else:
            print(f"Invalid operation! {piecee} does not exist in the collection.")

for track in composer_of_piece.keys():
    the_composer = composer_of_piece[track]
    the_key = key_of_piece[track]
    print(f"{track} -> Composer: {the_composer}, Key: {the_key}")
