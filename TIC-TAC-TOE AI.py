import math

# Initialize empty board
board = [" " for _ in range(9)]

# Print board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Check for winner
def check_winner(b, player):
    win_positions = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                     (0,3,6), (1,4,7), (2,5,8),  # Columns
                     (0,4,8), (2,4,6)]           # Diagonals
    for x, y, z in win_positions:
        if b[x] == b[y] == b[z] == player:
            return True
    return False

# Check for draw
def is_draw(b):
    return " " not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

# Best move for AI
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except:
            print("Please enter a number from 1 to 9.")
            continue

        board[move] = "X"
        print_board()

        if check_winner(board, "X"):
            print("You win! 🎉")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai = best_move()
        board[ai] = "O"
        print_board()

        if check_winner(board, "O"):
            print("AI wins! 😎")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

play_game()
