"""
Quick bruteforce chess library used to return dictionary
of possible chessmoves.
White chess pieces are represented as uppercase letters:
P -> Pawn   R -> Rook   H -> Knight
B -> Bishop K -> King   Q -> Queen

Black chess pieces are represented as uppercase letters:
p -> Pawn   r -> rook   h -> knight
b -> bishop k -> king   q -> queen
NB: knight = h -> "horse"
    Will possibly be changed later..

Chessboard must be 2D list with size 
NOTE: MUST BE PLAYED IN LIGHT MODE!
"""

# black = lowercase 
# white = UPPERCASE
white = list("PRHBKQ") # all possible white pieces
black = list("prhbkq") # all possible black pieces
xCordList = list("abcdefgh")
legalMovesWhite = dict() # dictionary of possible moves for white
legalMovesBlack = dict() # dictionary of possible moves for black
debugMode = False
gameActive = True

# piece data is stored as cordinate of piece, not name of piece
# cords are in format (y, x) due to list[0] giving y = 0
# and list[0][2] giving y = 0 and x = 3

# if I make a gui for this, the piece must be retrieved from 'board'
# possibly just taking a board, when file is imported
# and possible moves from legalMoves(black / white) dictionary
# board represented as 2D list

if __name__ == "__main__":
    board = list()
    board.append(["r","h","b","q","k","b","h","r"])
    board.append(["p","p","p","p","p","p","p","p"])
    board.append([" "," "," "," "," "," "," "," "])
    board.append([" "," "," "," "," "," "," "," "])
    board.append([" "," "," "," "," "," "," "," "])
    board.append([" "," "," "," "," "," "," "," "])
    board.append(["P","P","P","P","P","P","P","P"])
    board.append(["R","H","B","Q","K","B","H","R"])

# quick function to help represent chessboard values
# as a1, a2, ... , h7, h8
def cordToChesspos(y, x):
    """
    Takes cordinates in format (y, x) and returns in standard
    chess format. e.g. a1, c4
    """
    return str(xCordList[x]+str(8-(y)))
def chessposToCord(chesspos):
    """
    Takes standard chess input in format "a1, c4" and converts it to 
    this library's cordinate format (y, x)
    """
    chesspos = list(chesspos)
    return (8-int(chesspos[1]), int(xCordList.index(chesspos[0])))

# list of chessboard symbols as unicode characters
# only used for printing chessboard to shell
unicodePieces = {"P":"♙", "R":"♖", "H":"♘", "B":"♗", "K":"♔", "Q":"♕", " ":" ", "p":"♟︎", "r":"♜", "h":"♞", "b":"♝", "k":"♚", "q":"♛"}


# ============================================================================================
# # legal moves for pieces
# legal moves of black pawn
def legalMoveBlackPawn(y, x):
    """
    Bruteforce calulates all the possible moves for a pawn at the cordinates (x, y).
    NB: cordinates in function are reversed due to how the board is stored.
    NB: only works with black pawns if black starts on row 0 and 1
    """
    legalMoves = list()
    # checks if the square below it is open
    if board[y+1][x] == " ":
        legalMoves.append((y+1,x))
    if y == 1:
        if board[y+2][x] == " ":
            legalMoves.append((y+2,x))
    if x != 0: # checks if to the left
        # if not check if white to left
        if board[y+1][x-1] in white:
            legalMoves.append((y+1, x-1))
    if x != 7: # check if to the right
        # if not check if white to right
        if board[y+1][x+1] in white:
            legalMoves.append((y+1, x+1))
    return legalMoves

def legalMoveWhitePawn(y, x):
    """
    Bruteforce calulates all the possible moves for a pawn at the cordinates (x, y).
    NB: cordinates in function are reversed due to how the board is stored.
    NB: only works with white pawns if black starts on row 6 and 7
    """
    legalMoves = list()
    # checks if the square below it is open
    if board[y-1][x] == " ":
        legalMoves.append((y-1,x))
    if y == 6:
        if board[y-2][x] == " ":
            legalMoves.append((y-2,x))
    if x != 0: # checks if to the left
        # if not check if white to left
        if board[y-1][x-1] in black:
            legalMoves.append((y-1, x-1))
    if x != 7: # check if to the right
        # if not check if white to right
        if board[y-1][x+1] in black:
            legalMoves.append((y-1, x+1))
    return legalMoves

def legalMoveKing(y, x, opColor):
    legalMoves = list()
    # check position
    # 1: not top row
    if y != 0:
        # check up: y - 1
        if board[y-1][x] in opColor or board[y-1][x] == " ":
            legalMoves.append((y-1, x))

    # 2: not top right
    if x != 7 and y != 0:
        # check up right: y - 1, x + 1
        if board[y-1][x+1] in opColor or board[y-1][x+1] == " ":
            legalMoves.append((y-1, x+1))

    # 3: not most right column
    if x != 7:
        # check right: x + 1
        if board[y][x+1] in opColor or board[y][x+1] == " ":
            legalMoves.append((y, x+1))

    # 4: not bottom right corner
    if x != 7 and y != 7:
        # check down left: y + 1, x - 1
        if board[y+1][x+1] in opColor or board[y+1][x+1] == " ":
            legalMoves.append((y+1, x+1))
    
    # 5: not bottom row
    if y != 7:
        # check down: y + 1
        if board[y+1][x] in opColor or board[y+1][x] == " ":
            legalMoves.append((y+1, x))
    
    # 6: not bottom left
    if y != 7 and x != 0:
        # check down left: y + 1, x - 1
        if board[y+1][x-1] in opColor or board[y+1][x-1] == " ":
            legalMoves.append((y+1, x-1))
    
    # 7: not most left row
    if x != 0:
        # check left: x - 1
        if board[y][x-1] in opColor or board[y][x-1] == " ":
            legalMoves.append((y, x-1))
    
    # 8: not top left
    if x != 0 and y != 0:
        # check top left: y - 1, x - 1
        if board[y-1][x-1] in opColor or board[y-1][x-1] == " ":
            legalMoves.append((y-1, x-1))
            
    return legalMoves

def legalMoveRook(y, x, opColor):
    """
    Bruteforce calculates possible moves for a rook at the position (x, y)
    NB: opColor is color of opponent, name needs to correspond to the 
        list of opponent pieces found at initialization fase.
    NB: cordinates reversed due to board being a 2D list.
    """
    legalMove = list()
    yPositiveReached = False # up
    yNegativeReached = False # down
    xPositiveReached = False # right
    xNegativeReached = False # left
    # check up
    for i in range(y):
        if yPositiveReached == False:
            if board[y-1-i][x] in opColor or board[y-1-i][x] == " ":
                legalMove.append((y-1-i, x))
            if board[y-1-i][x] != " ":
                yPositiveReached = True
    # check down
    for i in range(7-y):
        if yNegativeReached == False:
            if board[y+1+i][x] in opColor or board[y+1+i][x] == " ":
                legalMove.append((y+i+1, x))
            if board[y+1+i][x] != " ":
                yNegativeReached = True
    # check right
    for i in range(7-x):
        if xPositiveReached == False:
            if board[y][x+1+i] in opColor or board[y][x+1+i] == " ":
                legalMove.append((y, x+1+i))
            if board[y][x+1+i] != " ":
                xPositiveReached = True
    # check left
    for i in range(x):
        if xNegativeReached == False:
            if board[y][x-1-i] in opColor or board[y][x-1-i] == " ":
                legalMove.append((y, x-1-i))
            if board[y][x-1-i] != " ":
                xNegativeReached = True
    return legalMove

def legalMoveBishop(y, x, opColor):
    """
    Bruteforce calculates possible moves for a bishop at the position (x, y)
    NB: opColor is color of opponent, name needs to correspond to the 
        list of opponent pieces found at initialization fase.
    NB: cordinates reversed due to board being a 2D list.
    """
    # appends all possible moves to legalMove list, 
    # is returned at end of function
    legalMove = list()
    
    # these functions stop the loops whenever a bishop has hit a obstacle, 
    # this obstacle can be either own piece or opponent piece
    upRightHit = False
    upLeftHit = False
    downRightHit = False
    downLeftHit = False
    # check up right
    # no point in checking if at the edge of the board
    # checks up right by iterating through list with x+1 -> and y-1 ^
    if (y != 0 and x != 7):
        for i in range(min(y,7-x)):
            if upRightHit == False:
                if board[y-1-i][x+1+i] in opColor or board[y-1-i][x+1+i] == " ":
                    legalMove.append((y-1-i, x+1+i))
                if board[y-1-i][x+1+i] != " ":
                    upRightHit = True
    # check up left 
    # checks up left by iterating through list with x-1 <- and y-1 ^
    if y != 0 and x != 0:
        for i in range(min(y, x)):
            if upLeftHit == False:
                if board[y-1-i][x-1-i] in opColor or board[y-1-i][x-1-i] == " ":
                    legalMove.append((y-i-1, x-1-i))
                if board[y-1-i][x-1-i] != " ":
                    upLeftHit = True
    # check down right
    # checks down right by iterating through list with x+1 -> and y+1 v
    if y != 7 and x != 7:
        for i in range(min(7-y,7-x)):
            if downRightHit == False:
                if board[y+1+i][x+1+i] in opColor or board[y+1+i][x+1+i] == " ":
                    legalMove.append((y+1+i, x+1+i))
                if board[y+1+i][x+1+i] != " ":
                    downRightHit = True
    # check down left
    # checks down left by iterating through list with x-1 <- and y+1 v
    if y != 7 and x != 0:
        for i in range(min(7-y, x)):
            if downLeftHit == False:
                if board[y+1+i][x-1-i] in opColor or board[y+1+i][x-1-i] == " ":
                    legalMove.append((y+1+i, x-1-i))
                if board[y+1+i][x-1-i] != " ":
                    downLeftHit = True
    return legalMove

def legalMoveKnight(y, x, opColor):
    legalMoves = list()
    # for each position, first check if it needs to be checked
    # up 1, delta x = 1
    if y >= 2:
        # up 1 left
        if x >= 1:
            if board[y-2][x-1] in opColor or board[y-2][x-1] == " ":
                legalMoves.append(((y-2, x-1)))
        if x <= 7:
            if board[y-2][x+1] in opColor or board[y-2][x+1] == " ":
                legalMoves.append(((y-2, x+1)))
    # up 2, delta x = 2
    if y >= 1:
        # up 2 left
        if x >= 2:
            if board[y-1][x-2] in opColor or board[y-1][x-2] == " ":
                legalMoves.append(((y-1, x-2)))
        # up 2 left
        if x <= 5:
            if board[y-1][x+2] in opColor or board[y-1][x+2] == " ":
                legalMoves.append(((y-1, x+2)))
    # down 1, delta x = 1
    if y <= 2:
        # down 1 left
        if x >= 1:
            if board[y+2][x-1] in opColor or board[y+2][x-1] == " ":
                legalMoves.append(((y+2, x-1)))
        if x <= 7:
            if board[y+2][x+1] in opColor or board[y+2][x+1] == " ":
                legalMoves.append(((y+2, x+1)))
    # down 2, delta x = 2
    if y <= 6:
        # up 2 left
        if x >= 2:
            if board[y+1][x-2] in opColor or board[y+1][x-2] == " ":
                legalMoves.append(((y+1, x-2)))
        # up 2 left
        if x <= 5:
            if board[y+1][x+2] in opColor or board[y+1][x+2] == " ":
                legalMoves.append(((y+1, x+2)))
    return legalMoves


# ============================================================================================
# for loop over pieces to find them and calculate legal moves
# NB: when implementing into game, remove the "{piece} @" from dictionary

def checkBoardBlack(board):
    """
    Takes 2D-list-chessboard as input and returns a dictionary "legalMovesBlack" 
    with all possible moves for each piece.
    Data is stored as a dictionary with key being the piece's (y, x)
    cordinate and the list containing all possible cordinates it can
    move to
    """
    for y in range(len(board)):
        for x in range(len(board[y])):
            # pawns
            if board[y][x] == "p":
                legalMovesBlack[str("P"+cordToChesspos(y,x))] = (legalMoveBlackPawn(y, x))
            
            # rook
            if board[y][x] == "r":
                legalMovesBlack[str("R"+cordToChesspos(y,x))] = (legalMoveRook(y, x, white))
            
            # bishop
            if board[y][x] == "b":
                legalMovesBlack[str("B"+cordToChesspos(y,x))] = (legalMoveBishop(y, x, white))
            
            # queen
            if board[y][x] == "q":
                legalMovesBlack[str("Q"+cordToChesspos(y,x))] = (legalMoveRook(y, x, white)) + (legalMoveBishop(y, x, white))
            
            # knight
            if board[y][x] == "h":
                legalMovesBlack[str("H"+cordToChesspos(y,x))] = (legalMoveKnight(y, x, white))

            # king
            if board[y][x] == "k":
                legalMovesBlack[str("K"+cordToChesspos(y,x))] = (legalMoveKing(y, x, white))

def checkBoardWhite(board):
    """
    See description of checkBoardBlack
    """
    for y in range(len(board)):
        for x in range(len(board[y])):
            # pawns
            if board[y][x] == "P":
                legalMovesWhite[str("P"+cordToChesspos(y,x))] = (legalMoveWhitePawn(y, x))
            
            # rook
            if board[y][x] == "R":
                legalMovesWhite[str("R"+cordToChesspos(y,x))] = (legalMoveRook(y, x, black))

            # bishop
            if board[y][x] == "B":
                legalMovesWhite[str("B"+cordToChesspos(y,x))] = (legalMoveBishop(y, x, black))

            # queen
            if board[y][x] == "Q":
                legalMovesWhite[str("Q"+cordToChesspos(y,x))] = (legalMoveRook(y, x, black)) + (legalMoveBishop(y, x, black))

            # knight
            if board[y][x] == "H":
                legalMovesWhite[str("H"+cordToChesspos(y,x))] = (legalMoveKnight(y, x, black))
            
            # king
            if board[y][x] == "K":
                legalMovesWhite[str("K"+cordToChesspos(y,x))] = (legalMoveKing(y, x, black))

def removeKingChecksBlack():
    notKingChecks = list()
    whiteMoves = list()
    for i in legalMovesWhite.values():
        for value in i:
            whiteMoves.append(value)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "k":
                if legalMovesBlack.get(str(f"King @ ({y}, {x})")) != None:
                    kingMoves = legalMovesBlack.get(str(f"King @ ({y}, {x})"))
                    for pos in kingMoves:
                        if pos not in whiteMoves:
                            notKingChecks.append(pos)
                    legalMovesBlack[str(f"King @ ({y}, {x})")] = notKingChecks

def removeKingChecksWhite():
    notKingChecks = list()
    blackMoves = list()
    for i in legalMovesBlack.values():
        for value in i:
            blackMoves.append(value)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "K":
                if legalMovesWhite.get(str(f"King @ ({y}, {x})")) != None:
                    kingMoves = legalMovesWhite.get(str(f"King @ ({y}, {x})"))
                    for pos in kingMoves:
                        if pos not in blackMoves:
                            notKingChecks.append(pos)
                    legalMovesWhite[str(f"King @ ({y}, {x})")] = notKingChecks


# ============================================================================================

# print out possible moves
def printPossibleMoves(black, white):
    """
    After the checkBoard-functions have been excecuted this command will return
    all possible moves as standard chess cordinates, e.g. a1, c4
    """
    print("\nPossible moves for black:")
    for key, value in black.items():
        cordValue = ""
        for i in value:
            cordValue += cordToChesspos(i[0],i[1]) + " "
        cordValue = cordValue.split(" ")
        cordValue.pop(-1)
        print(f"{key}    ->    {cordValue}")
    print("\n", "="*50, "\n")
    print("Possible moves for white:")
    for key, value in white.items():
        cordValue = ""
        for i in value:
            cordValue += cordToChesspos(i[0],i[1]) + " "
        cordValue = cordValue.split(" ")
        cordValue.pop(-1)
        print(f"{key}    ->    {cordValue}")

# draw board as unicode chess pieces
def printBoard(board):
    """
    Prints chessboard to shell using unicode characters for chesspieces
    Only intended used when debugging
    """
    rowCount = 8
    print("")
    for row in board:
        rowPieces = ""
        for piece in row:
            if piece != " ":
                rowPieces += "\u0332".join((unicodePieces[piece])) + "|"
            else:
                rowPieces += "_" + "|"
        print(f"{rowCount}: "+ str(rowPieces))
        rowCount -= 1
    print("   A B C D E F G H")
    print("")

# clear screen
def cls():  
    """
    Clear screen function
    """     
    print("\n" * 100)

# ignore for now
def checkBoard(board):
    """
    Function to be imported into chess.py
    """
    checkBoardBlack(board)
    checkBoardWhite(board)

    removeKingChecksBlack()
    removeKingChecksWhite()

if __name__ == "__main__" and debugMode == True:
    # time it for performance metrics
    import time
    # time used to print out is irrelevant for the performance
    # therefore, we only time the processing of the board
    timeBefore = time.time()

    # perform the check
    # will later be called after each move
    checkBoard(board)

    timeAfter = time.time()
    # avg should be around 0.08 ms, ignores time for printing
    # later, if there are any performance issues, legalMovesChess, 
    # shouldn't need to be optimized

    # only to be run when debugging or implementing new features
    printPossibleMoves(legalMovesBlack, legalMovesWhite)
    print("\n")
    print(f"Finished calculating possible moves in {round((timeAfter-timeBefore)*1000,2)}ms")


# ============================================================================================
# need to implement ability to move pieces

def whiteMove():
    print("Format: {piece} {destination}")
    print("Example: Qa1 d4")
    print("To print out possible moves, type 'list moves'")
    userMove = input("WHITE MOVE > ")
    # check if they want to list moves
    if userMove == "list moves":
        cls()
        printPossibleMoves(legalMovesBlack,legalMovesWhite)
        printBoard(board)
        whiteMove()
    elif userMove == ("quit" or "exit"):
        exit()
    # check if move is in list
    else:
        try:
            userMove = userMove.split(" ")
            piecePos = userMove[0]
            piecePosCord = list(chessposToCord(str(piecePos[1:])))
            y = piecePosCord[0]
            x = piecePosCord[1]
            move = chessposToCord(str(userMove[1]))
            if move in legalMovesWhite[piecePos]:
                # perform board manipulation to perform move
                board[y][x] = " "
                board[int(move[0])][int(move[1])] = str(userMove[0][0]).upper()
            else:
                print("Not possible move idot, try 'list moves'")
                whiteMove()
        except:
            print("Honestly, use the correct notation!")
            whiteMove()


def blackMove():
    print("Format: {piece} {destination}")
    print("Example: Qa1 d4")
    print("To print out possible moves, type 'list moves'")
    userMove = input("BLACK MOVE > ")
    # check if they want to list moves
    if userMove == "list moves":
        cls()
        printPossibleMoves(legalMovesBlack,legalMovesWhite)
        printBoard(board)
        blackMove()
    elif userMove == ("quit" or "exit"):
        exit()
    # check if move is in list
    else:
        try:
            userMove = userMove.split(" ")
            piecePos = userMove[0]
            piecePosCord = list(chessposToCord(str(piecePos[1:])))
            y = piecePosCord[0]
            x = piecePosCord[1]
            move = chessposToCord(str(userMove[1]))
            if move in legalMovesBlack[piecePos]:
                # perform board manipulation to perform move
                board[y][x] = " "
                board[int(move[0])][int(move[1])] = str(userMove[0][0]).lower()
            else:
                print("Not possible move idot, try 'list moves'")
                blackMove()
        except:
            print("Honestly, use the correct notation!")
            blackMove()

def oneRound():
    cls()
    checkBoard(board)
    printBoard(board)
    whiteMove()

    cls()
    checkBoard(board)
    printBoard(board)
    blackMove()
    # check if usermove is within the dictionary
    # if not, repeat, if within make move
    # move can be made by changing the original piecepos to " "
    # and setting the new piecepos to the piece letter, eg. "q" or "R"

# game plays
while gameActive == True:
    oneRound()
