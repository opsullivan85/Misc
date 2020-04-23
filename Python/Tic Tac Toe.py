
print "Welcome to Tic Tac Toe"
board = []

for num in range(3):
    board.append(["_"] * 3)

def show(board):
    for list in board:
        print "  ".join(list)



show(board)


def player_X_Move():

    print ""
    print ""

    print "It Is Player X's Turn"
    
    player_X_Col = int(raw_input("Col (1 - 3):  ")) -1
    player_X_Row = 3 - int(raw_input("Row (1 - 3):  "))

    if (player_X_Row < 0 or player_X_Row > 4) or (player_X_Col < 0 or player_X_Col > 4):
        print "ONE THROUGH THREE! Try again."
        show(board)
        player_X_Move()
    elif board[player_X_Row][player_X_Col] == "X" or board[player_X_Row][player_X_Col] == "O":
        print "That square is already taken. Try again."
        show(board)
        player_X_Move()
    else:
        board[player_X_Row][player_X_Col] = "X"
        show(board)



def player_O_Move():

    print ""
    print ""

    print "It Is Player O's Turn"
    
    player_O_Col = int(raw_input("Col (1 - 3):  ")) -1
    player_O_Row = 3 - int(raw_input("Row (1 - 3):  "))

    if (player_O_Row < 0 or player_O_Row > 4) or (player_O_Col < 0 or player_O_Col > 4):
        print "ONE THROUGH THREE! Try again."
        show(board)
        player_O_Move()
    elif board[player_O_Row][player_O_Col] == "X" or board[player_O_Row][player_O_Col] == "O":
        print "That square is already taken. Try again."
        show(board)
        player_O_Move()
    else:
        board[player_O_Row][player_O_Col] = "O"
        show(board)



def game():
    player_X_Move()
    player_O_Move()
    game()


game()


    
