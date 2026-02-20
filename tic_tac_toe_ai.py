# Tic-Tac-Toe AI using Minimax Algorithm
# Human is X, AI is O

# Initialize board
board = [' ' for _ in range(9)]

# Display the board
def display_board(board):
    print()
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print()

# Check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Human move
def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8:
                print("Invalid input! Enter a number 0-8.")
            elif board[move] != ' ':
                print("Cell already taken! Choose another.")
            else:
                board[move] = 'X'
                break
        except ValueError:
            print("Invalid input! Enter a number 0-8.")

# AI move using Minimax
def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Minimax function
def minimax(board, is_maximizing):
    if check_winner(board, 'O'):
        return 10
    elif check_winner(board, 'X'):
        return -10
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Main game loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    print("Positions are numbered 0-8 as below:")
    print("0|1|2\n-+-+-\n3|4|5\n-+-+-\n6|7|8\n")

    while True:
        display_board(board)
        human_move(board)
        if check_winner(board, 'X'):
            display_board(board)
            print("Congratulations! You win!")
            break
        elif ' ' not in board:
            display_board(board)
            print("It's a draw!")
            break

        ai_move(board)
        if check_winner(board, 'O'):
            display_board(board)
            print("AI wins! Better luck next time.")
            break
        elif ' ' not in board:
            display_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()