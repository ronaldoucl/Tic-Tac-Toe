from random import randrange

def init_board():
    return [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]

def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(row) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    move = input("Enter your movement: ")
    while not (move.isdigit() and 1 <= int(move) <= 9 and board[(int(move)-1)//3][(int(move)-1)%3] not in ['O', 'X']):
        move = input("Invalid move, try again: ")
    board[(int(move)-1)//3][(int(move)-1)%3] = 'O'

def draw_move(board):
    move = randrange(9)
    while board[move // 3][move % 3] in ['O', 'X']:
        move = randrange(9)
    board[move // 3][move % 3] = 'X'

def victory_for(board, sign):
    # Check rows, columns and diagonals
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2-i] == sign for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] in ['O', 'X'] for i in range(3) for j in range(3))

def main():
    board = init_board()
    display_board(board)
    board[1][1] = 'X' # First movement of the machine
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("¡YOU'VE WON!")
            break
        if is_board_full(board):
            print("Tie")
            break
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("The machine wins!")
            break

main()
