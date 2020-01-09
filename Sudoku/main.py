
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0:
                print("|", end="")

            if j == 8:
                print(str(board[i][j])+"|")
            else:
                print(str(board[i][j]) + " ", end="")


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid_board(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return (x, y)  # row and col
    return None


def valid_board(board, num, pos):
    # validate row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
# validate colom
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
# validate box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True
