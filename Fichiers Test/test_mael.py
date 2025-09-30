import random

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

def choix_ordinateur(nb_objet):
    # Stratégie gagnante : laisser un multiple de 4 à l'adversaire
    if nb_objet % 4 == 0:
        return 1
    else:
        return nb_objet % 4

def partie_vs_ordinateur():
    nb_allumette = 20
    ordinateur = random.randint(1, 2)
    saut_de_ligne(1)
    print("L'ordinateur est le joueur numéro ", ordinateur)
    separateur('-')
    affichage(nb_allumette, '*') 
    while nb_allumette > 0:
        if prochain_joueur(ordinateur) == 1:
            n = choix_joueur()
            print(f"Le joueur numéro {prochain_joueur(ordinateur)} enlève {n} objets")
            nb_allumette -= n
            affichage(nb_allumette, '*')
            saut_de_ligne(1)
            separateur('-')
        else:
            n = choix_ordinateur(nb_allumette)
            print(f"L'ordinateur enlève {n} objets")
            nb_allumette -= n
            affichage(nb_allumette, '*')
        ordinateur = prochain_joueur(ordinateur)
    if ordinateur == 1:
        print("L'ordinateur gagne !")
    else:
        print("Joueur", prochain_joueur(ordinateur), "gagnant !")
    return

# Pour jouer contre l'ordinateur, décommentez la ligne suivante :
# partie_vs_ordinateur()
# Pour corriger le problème, il faut s'assurer que la fonction partie_vs_ordinateur() est appelée.
# Décommentez la ligne suivante pour jouer contre l'ordinateur :

partie_vs_ordinateur()