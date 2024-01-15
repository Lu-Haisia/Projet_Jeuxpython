from random import randint

def newBoard(n, p):
    board = []
    for i in range(n):
        board.append(randint(0, p))   
    return board


def display(board, n):
    separation = []
    index = []
    for i in range(n):
        index.append(i+1)
        separation.append('--')
    print(*board, sep='  | ', end=' |\n')
    print(*separation, sep='---', end='\n')
    print(*index,  sep='  | ', end=' |\n')


def somme(board,n,p):
    _somme = 0
    for i in board:
        _somme = _somme + i
    if _somme == 0 or _somme == 1 :
        while _somme == 0 or  _somme == 1  : 
            newBoard(n,p)
    return _somme

# Une fonction qui permet de calculer le nombre de pion sur le plateau, si il n'y as pas de pion, ou un seul, il relance le newbord

def nimble(board, n, p, player1, player2): 
    player = player1
    if lose(board, n,p) == False :
        while lose(board,n,p) == False :
            print("Player", player)
            i = int(input("Choisir une case pour le déplacement : ")) - 1 # -1 pour obtenir l'index par rapport à l'index du display
            while not possibleSquarre(board, i):
                i = int(input("Pas de pions disponibles, choisir une autre case : ")) - 1
            print("Case", i + 1, "remplie, déplacements possibles")

            j = int(input("Choisir une case de destination : ")) - 1
            while not possibleDestination(board, i, j):
                j = int(input("Déplacement impossible, choisir une autre case : ")) - 1
            print("Le déplacement vers la case", j + 1, "est possible")

            move(board, i, j)
            display(board, nombren)

            if lose(board,n,p):
                break
            # Quand la condition de lose est valide, on arrête le programme ici, sinon il continu
            if player == player1:
                player = player2
            else:
                player = player1
    print("Joueur "+str(player)+" gagne.")

def possibleSquarre(board, i):
    if board[i] == 0 or i == 0: 
        return False
    else : 
        return True


def selectSquare(board, i):
    if possibleSquarre(board,i) == False : 
        while possibleSquarre(board,i) == False : 
            i = int(input("Pas de pions disponibles, choisir une autre case : "))-1
    print("Case",i+1, "remplie, déplacements possibles")
    return

    
def possibleDestination(board, i,j):
    if i < j or board[i]==0 or j == -1: 
        return False
    else :
        return True


def selectDestination(board, i,j):
    if possibleDestination(board,i,j) == False: 
        while possibleDestination(board,i,j) == False : 
            j = int(input("Deplacement impossible, choisir une autre case : "))-1
    print("Le déplacement vers la case",j+1, "est possible")
    return


def move(board, i, j):
    if possibleDestination(board,i,j) == True :
        board[j] = board[j]+1
        board[i] = board[i]-1
    return


def lose(board,n,p):
    if  board[0] != somme(board,n,p):
        return False
    else :
        print("Partie Terminée")
        return True 

#############################################

nombren = int(input("[Initialisation] Taille du plateau (n) "))
nombrep =  int(input("[Initialisation] Nombre max de pions (p) "))
player1 = (input("[Initialisation] Joueur 1 "))
player2 = (input("[Initialisation] Joueur 2 "))
# On définit au départ, la taille du plateau, le nombre de pion max par cases, et le nom des joueurs


board= newBoard(nombren , nombrep)
display(board, nombren)
nimble(board, nombren, nombrep, player1, player2)
