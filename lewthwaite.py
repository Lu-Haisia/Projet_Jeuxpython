def newBoard(n):
    index=1
    board = []
    for i in range(n):
        ligne=[]
        board.append(ligne)
        if index % 2 == 0 :
            for i in range(n):
                ligne.append(1)
                ligne.append(2)
            if len(ligne) != n :
                while len(ligne) != n :
                    ligne.pop()
                        
        else :
            for i in range(n):
                ligne.append(2)
                ligne.append(1)
            if len(ligne) != n :
                while len(ligne) != n :
                    ligne.pop()
        index+=1
        
    j = int((n-1) / 2)
    i = int((n-1) / 2)
    board[i][j] = 0
    return board

        
def displayBoard(board, n) :
    index= []
    separation = []

    for i in range(0, n):
        separation.append('--')

    for i in range(0, n+1):
        index.append(i)

    for i in range(n):
        print(i+1, "|", end=" ")
        for j in range(n):
            if board[i][j]== 1 : 
                print('x',end="   ")
            elif  board[i][j]== 2:
                print('o',end="   ")
            elif board[i][j] == 0 :
                print('.',end="   ")
        print(end=" \n")
        
    print(*separation, sep='---', end='\n')
    print(*index, sep="   ")
    return

###
def zeroi(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i + 1


def zeroj(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return j + 1
# Ces deux fonctions permettent de trouver le zero à chaque nouveau display


def lewthwaite(board,n, cori,corj) : 
    player1 = 1
    player2 = 2
    player = player1
    i,j=0,0
    if again(board,player,n, cori,corj)== True :
        while again(board,player,n, cori,corj)== True :
            print("Player", player)   

            i,j = selectPawn(board, i, j,player)
            while possiblePawn(board, i, j, player) == False :
                i,j = selectPawn(board, i, j,player)

            updateBoard(board, i, j, cori, corj,player) 
            displayBoard(board, n)
            cori= zeroi(board)
            corj = zeroj(board)
            if again(board,player,n, cori,corj)== False :
                break
        
            if player == player1:
                player = player2
            else:
                player = player1
    print("Joueur "+str(player)+" gagne.")
    return

def possiblePawn(board, i, j, player):
    player1 = 1
    player2 = 2
    if player == player2 and board[i][j] == 2 or player == player1 and board[i][j] == 1:
        return True
    else:
            return False

def selectPawn(board, i, j,player): 
    i = int(input("Choisir une coordonée i : "))-1
    j = int(input("Choisir une coordonée j : "))-1
    while possiblePawn(board, i, j, player) == False:
        i = int(input("Choisir le pion i de la bonne couleur ou a proximité de la case vide : "))-1
        j = int(input("Choisir le pion j de la bonne couleur ou a proximité de la case vide : "))-1
    return i , j

def updateBoard(board, i, j, cori,corj,player) :
    cori -= 1
    corj -= 1
    if possiblePawn(board,i,j, player) == True:
        echange1 = board[i][j]
        echange2 = board[cori][corj]
        board [i][j] = echange2
        board[cori][corj] = echange1
    return  board[cori][corj]

def again(board,player,n, cori,corj): 
    if cori != 0 and board[cori-2][corj-1] == player :
        return True 

    if cori != n and board[cori][corj-1] == player :
        return True

    if corj != 0  and board[cori-1][corj-2]==player :
        return True
    
    if corj != n and board[cori-1][corj]== player :
        return True

    return False

       
#############################################
n = int(input("[Initialisation] Taille n : 4*n+1 : "))
while n <=0 :
    n = int(input("Reselectionner une taille n : 4*n+1 : "))
n = 4*n+1  


board = newBoard(n)
cori= zeroi(board)
corj = zeroj(board)
displayBoard(board, n)
lewthwaite(board,n, cori, corj)


