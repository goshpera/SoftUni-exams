rows, cols = [int(x) for x in input().split(",")]

matrix = []
mouse_pos = None
cheese_pieces = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    matrix.append(list(input()))

    if "M" in matrix[row]:
        mouse_pos = [row, matrix[row].index("M")]
        matrix[row][mouse_pos[1]] = "*"
    cheese_pieces += matrix[row].count("C")

while True:
    direction = input()
    if direction == "danger":
        print("Mouse will come back later!")
        break

    #row = mouse_pos[0] + directions[direction][0]
    #col = mouse_pos[1] + directions[direction][1]
    # TODO : add logic and solve the task
    row, col = mouse_pos
    new_row, new_col = row + directions[direction][0], col + directions[direction][1]

    if not (0 <= row < rows and 0 <= col < cols):
        print("No more cheese for tonight!")
        break

    #mouse_pos = [row, col]
    position = matrix[row][col]
    if matrix[new_row][new_col] == "*":
        matrix[row][col] = "*"
        matrix[new_row][new_col] = "M"
    elif position == "C":
        matrix[row][col] = "*"
        matrix[new_row][new_col] = "M"
        cheese_pieces -= 1
        if cheese_pieces == 0:
            print("Happy mouse!")
            break
    elif position == "T":
        matrix[row][col] = "M"
        print("Mouse is trapped!")
        break
    elif position == "@":
        continue


print(*[''.join(row) for row in matrix], sep="\n")

