# Simple Tic Tac Toe Game
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

for turn in range(9):
    print_board(board)
    row = int(input(f"{current_player}, enter row (0-2): "))
    col = int(input(f"{current_player}, enter column (0-2): "))

    if board[row][col] == " ":
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Cell already taken! Try again.")
else:
    print("It's a draw!")
