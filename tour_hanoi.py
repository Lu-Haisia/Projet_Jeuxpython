essaies = 0
def creationtours(n):
    tower = []
    tower1 = []
    tower2 = []
    tower3 = []

    for i in range(n): 
        tower1.append(i+1)
    tower = [tower1, tower2, tower3]
    return tower

def afficher_tours(tower):
    for i, tour in enumerate(tower):
        print(f"\033[1;33;40mTour {i + 1}: {tour}")
    

def processhanoi(n,d,a,i,tower):
    global essaies
    if n!=0: 
        essaies +=1
        processhanoi(n-1,d,i,a,tower)
        print("-----")
        print("\033[1;36;40mLe disque",n,"est déplacé de la tour\033[1;31m",d+1, "\033[1;36mvers la tour\033[1;31m", a+1)
        toura = tower[a]
        tourd = tower[d]
        xchange(tower,toura, tourd,n)
        afficher_tours(tower)
        processhanoi(n-1,i,a,d,tower)          

def xchange(tower,toura, tourd, n):
    retrait = tourd.pop(0)
    toura.insert(0, retrait)
    return tower

#n = (int(input("Nombre max de disques : ")))
n = 10


creationtours(n)

processhanoi(n,0,2,1, creationtours(n))
print("Réussi en ",essaies ,"essaies")
