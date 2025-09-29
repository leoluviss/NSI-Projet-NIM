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

def choix_joueur():
    saut_de_ligne(1)
    separateur('-')
    n=0
    while not (1 <= n <= 3):
        n = int(input("Nombre d'objets retirés ? "))
        if n < 1 or n > 3:
            print("Choisir un nombre d'objets entre 1 et 3.")
    return n

def prochain_joueur(joueur):
    assert joueur == 1 or joueur == 2
    if joueur == 1:
        return 2
    else:
        return 1

assert prochain_joueur(1) == 2
assert prochain_joueur(2) == 1

def partie_fort_boyard1():
    nb_objet = 20
    joueur = 1
    affichage(nb_objet, '*')
    while nb_objet > 0:
        n = choix_joueur()
        print(f"Le joueur numéro {joueur} enlève {n} objets")
        nb_objet -= n
        affichage(nb_objet, '*')
        joueur = prochain_joueur(joueur)
    print("Joueur", prochain_joueur(joueur), "gagnant !")
    return
partie_fort_boyard1()