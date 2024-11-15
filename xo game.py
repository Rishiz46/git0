# Simple Tic-Tac-Toe Game in Python

# Function to print the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Check diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Check other diagonal
        return True
    return False

# Function to check if the board is full (draw)
def board_full(board):
    return all([cell != " " for row in board for cell in row])

# Function to handle the player's turn
def player_turn(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0  # 0 for Player X, 1 for Player O

    while True:
        print_board(board)
        player = players[turn % 2]
        player_turn(board, player)
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1  # Switch to the other player

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
