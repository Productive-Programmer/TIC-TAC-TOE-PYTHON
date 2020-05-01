# TIC_TAC_TOE_PYTHON


# Defining the board
board = {'b1': ' ', 'b2': ' ', 'b3': ' ',
         'b4': ' ', 'b5': ' ', 'b6': ' ',
         'b7': ' ', 'b8': ' ', 'b9': ' '}

# Printing the board


def printBoard(board):
    print(f"{board['b1']} | {board['b2']} | {board['b3']}  ")
    print("--+---+--")
    print(f"{board['b4']} | {board['b5']} | {board['b6']}  ")
    print("--+---+--")
    print(f"{board['b7']} | {board['b8']} | {board['b9']}  ")

# Validating the move


def isvalid(pos):
    for i in board:
        if board[f'b{pos}'] == ' ':
            return True
        else:
            return False

# Movements on the board


def movements(pos, letter):

    for i in board:
        board[f"b{pos}"] = letter

# Checking the winner


def iswinner(letter):
    if board['b1'] == board['b2'] == board['b3'] == letter:
        return True
    elif board['b4'] == board['b5'] == board['b6'] == letter:
        return True
    elif board['b7'] == board['b8'] == board['b9'] == letter:
        return True
    elif board['b1'] == board['b4'] == board['b7'] == letter:
        return True
    elif board['b2'] == board['b5'] == board['b8'] == letter:
        return True
    elif board['b3'] == board['b6'] == board['b9'] == letter:
        return True
    elif board['b1'] == board['b5'] == board['b9'] == letter:
        return True
    elif board['b3'] == board['b5'] == board['b7'] == letter:
        return True
    else:
        return False


# Boolean variables for player switching
isO = False
isX = True
count = 0
# Boolean
while True:
    if isX:
        print("X turn!!")
        num = input("Enter the number:")
        if not isvalid(num):
            print("NOT A VALID MOVE!!")

        if isvalid(num):
            count += 1
            movements(num, 'X')
            printBoard(board)
            if count == 9:
                print("TIE GAME!!!!")
                break

            if iswinner('X'):
                print("X wins!!")
                break
            else:
                isO = True
                isX = False
    if isO:
        print("O turn!!!")
        num = input("Enter the number:")
        if not isvalid(num):
            print("NOT A VALID MOVE!!")

        if isvalid(num):
            # Checking the count for tie game
            count += 1
            movements(num, 'O')

            printBoard(board)
            if count == 9:
                print("TIE GAME!!!!")
                break

            if iswinner('O'):
                print("O wins!!")
                break
            else:
                isO = False
                isX = True
