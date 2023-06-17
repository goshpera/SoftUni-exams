def check_indices(r, c, row, col):  # function to check if the mouse is in the matrix
    if 0 <= r < row and 0 <= c < col:
        return True

    return False


rows, cols = [int(x) for x in input().split(",")]  # inputting the dimensions of the matrix

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []

mouse_position = []
cheese_pieces = 0

for row in range(rows):
    matrix.append([x for x in input()])  # adding row-times new lines to the matrix

    if "M" in matrix[row]:  # look where is the mouse position
        mouse_position = [row, matrix[row].index("M")]  # index it
        matrix[row][mouse_position[1]] = "*"

    if "C" in matrix[row]:  # finds all the cheese pieces in the matrix
        cheese_pieces += matrix[row].count("C")  # sums the total count

while True:
    direction = input()

    if direction == "danger":
        print("Mouse will come back later!")
        matrix[mouse_position[0]][mouse_position[1]] = "M"  # save the last position
        break

    new_row = mouse_position[0] + directions[direction][0]
    new_col = mouse_position[1] + directions[direction][1]

    if not check_indices(new_row, new_col, rows, cols):  # check if the mouse leaves the matrix
        matrix[mouse_position[0]][mouse_position[1]] = "M"  # save the last position
        print("No more cheese for tonight!")
        break

    if matrix[new_row][new_col] == "C":  # if we step on a cheese
        matrix[new_row][new_col] = "*"  # we eat it
        cheese_pieces -= 1
        if cheese_pieces == 0:  # if there is no more cheese in the matrix
            matrix[new_row][new_col] = "M"  # we place the mouse on the last position and end the program
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[new_row][new_col] == "@":
        continue  # ignore the @'s around the matrix
    elif matrix[new_row][new_col] == "T":  # if we step on a trap
        matrix[new_row][new_col] = "M"  # we place the mouse on the last position and end the program
        print("Mouse is trapped!")
        break

    mouse_position = [new_row, new_col]

for row in matrix:
    print(''.join(row))
