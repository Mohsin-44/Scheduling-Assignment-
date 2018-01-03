def Print(pos):
         print("\t" + board[0] + " | " + board[1] + " | " + board[2])
         print("\t" + board[3] + " | " + board[4] + " | " + board[5])
         print("\t" + board[6] + " | " + board[7] + " | " + board[8])
         
def getMark(turn):
    if turn%2==0:
        mark="X"
    else:
        mark="O"
    return mark

def checkReserved(board,index,turn):
    if (not index.isdecimal()) or int(index)<1 or int(index)>9:
        print("Invalid position selected")
        return 0
    if board[int(index)-1]=="X" or board[int(index)-1]=="O":
        print("Place already reserved ,try another place")
        return 0
    else:
         board[int(index)-1]=getMark(turn)
         return 1
        
def getTurn(turn):
    if turn%2==0:
        return 1
    else:
        return 2
    
def checkWin(board):
    win="false"
    if board[0]==board[1] and board[1]==board[2] or board[3]==board[4] and board[4]==board[5] or board[6]==board[7] and board[7]==board[8]:
        win="true"
    if board[0]==board[3] and board[3]==board[6] or board[1]==board[4] and board[4]==board[7] or board[2]==board[5] and board[5]==board[8]:
        win="true"
    if board[0]==board[4] and board[4]==board[8] or board[2]==board[4] and board[4]==board[6]:
        win="true"
    return win

board=[]
for i in range (1,10):
        board.append(str(i))
Print(board)
for turn in range(9):
    value=0
    while int(value)<1 or int(value)>9:
        print("Select a number between 1 and 9")
        print("Player %d turn: " % getTurn(turn),end="")
        value=input()
        if checkReserved(board,value,turn)==0:
            value=0
        Print(board)
    if turn>3:
        if checkWin(board)=="true":
            print("Player %d Wins!!!!!" % (getTurn(turn)))
            break
if(checkWin(board)=="false"):
    print("Game Draw!!!!")
