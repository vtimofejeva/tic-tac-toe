import random


board = ["1","2","3",
        "4", "5", "6",
        "7","8","9"]
pc_player = "X"
user_player = "O"
gameRunning = True

def display_board(board):
    print(" +-------+-------+-------+")
    print(" |       |       |       | ")
    print(" |   " +board[0] + "   |   " + board[1] + "   |   " + board[2] + "   |")
    print(" |       |       |       | ")
    print(" +-------+-------+-------+")
    print(" |       |       |       | ")
    print(" |   " +board[3] + "   |   " + board[4] + "   |   " + board[5] + "   |")
    print(" |       |       |       | ")
    print(" +-------+-------+-------+") 
    print(" |       |       |       | ")
    print(" |   " +board[6] + "   |   " + board[7] + "   |   " + board[8] + "   |")
    print(" |       |       |       | ")
    print(" +-------+-------+-------+")
# display_board(board)

def enter_move(board):
    user_select = int(input("Enter your move: "))
    if user_select >= 1 and user_select <= 9 and board[user_select-1] != "X" and board[user_select-1] != "O":
        board[user_select-1] = user_player    
    elif user_select < 1 or user_select > 9:
        print("Integers between 1 and 9 only are!") 
        enter_move(board)
    elif board[user_select-1] == "X" and user_select >= 1 and user_select <= 9:
        print("The PC marked that spot already!")
        enter_move(board)
    elif board[user_select-1] != "O" and user_select >= 1 and user_select <= 9:
        print("You already have selected this spot!")
        enter_move(board)    

def pc_turn():
    pc_select = random.randint(1,10)
    if pc_select >= 1 and pc_select <= 9 and board[pc_select-1] != "X" and board[pc_select-1] != "O":
        board[pc_select-1] = pc_player    
    else:
        pc_turn()

# define Win state:

def win_horizontal():
    if board[0:3] == ["X", "X", "X"] or board[3:6] == ["X", "X", "X"] or board[6:9] == ["X", "X", "X"]:
        display_board(board)
        print("PC won!")
        return False
    if board[0:3] == ["O", "O", "O"] or board[3:6] == ["O", "O", "O"] or board[6:9] == ["O", "O", "O"]:
        display_board(board)
        print("You won_H!")
        return False

def win_vertical():
    if board[0] == "X" and board[3] == "X" and board[6] == "X"\
    or board[1] == "X" and board[4] == "X" and board[7] == "X"\
    or board[2] == "X" and board[5] == "X" and board[8] == "X":
        display_board(board)
        print("PC won!")
        return False
    if board[0] == "O" and board[3] == "O" and board[6] == "O"\
    or board[1] == "O" and board[4] == "O" and board[7] == "O"\
    or board[2] == "O" and board[5] == "O" and board[8] == "O":
        display_board(board)
        print("You won_V!")
        return False
    
def win_diagonal():
    if board[0] == "X" and board[4] == "X" and board[8] == "X"\
    or board[2] == "X" and board[6] == "X" and board[6] == "X":
        display_board(board)
        print("PC won!")
        return False
    if board[0] == "O" and board[4] == "O" and board[8] == "O"\
    or board[2] == "O" and board[6] == "O" and board[6] == "O":
        display_board(board)
        print("You won!_D")    
        return False

# printing the game board
# showing the first PC's move, which is always in the middle
# take player input and return the result
# check for win or tie
# switch the player
# check for win or tie again

display_board(board)
print("First goes PC and marks the middle (5)")
board[4] = pc_player

while gameRunning:
    display_board(board)
    
    enter_move(board)
    if win_diagonal() == False or win_horizontal() == False or win_vertical() == False:
        gameRunning = False
        break
    
    pc_turn()
    if win_diagonal() == False or win_horizontal() == False or win_vertical() == False:
        gameRunning = False
        break

        
