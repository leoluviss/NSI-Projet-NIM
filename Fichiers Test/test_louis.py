def separateur(caractere):
    for loop in range(80):
        print(caractere, end="")
    print("")
    return
    
def saut_de_ligne(n):
    for loop in range(n):
        print("")
    return

def affichage(n, caractere):
    saut_de_ligne(1)    
    separateur('-')
    print(f"{n} objets restants : ")
    for loop in range(n):
        print(caractere, end=" ")
    print("")
    separateur('-')
    saut_de_ligne(1)
    return

affichage(5, '*')
