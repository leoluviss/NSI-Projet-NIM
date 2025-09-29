#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet 1 : jeu de Nim
Squelette de la partie 1 
"""

#%% Simulation d'un duel des batonnets avec deux joueurs humains
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


#%%

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

#%% Simulation d'un duel des batonnets avec un joueur humain jouant contre l'ordinateur

#import du module random
import random

def choix_ordinateur(nb_objet):
    """
    Renvoie le choix de l'ordinateur 
    (1,2 ou 3 objets enlevés)
    s'il reste nb_objet objets
    stratégie gagnante si possible
    choix aléatoire sinon

    Args:
        nb_objet : int 
                nombre d'objets restants

    Returns:
        int: nombre d'objets retirés
    """
    #à compléter

#Tests unitaires 
assert choix_ordinateur(18) == 2
assert choix_ordinateur(15) == 3
assert choix_ordinateur(3) == 3
assert choix_ordinateur(9) ==1

def partie_fort_boyard2():
    """
    Simule une partie du jeu des allumettes
    de Fort Boyard entre deux joueurs humains
    20 allumettes au départ 
    A chaque tour, un joueur prend entre 1 et 3 allumettes
    Celui qui ne peut plus jouer a perdu    
    Affiche l'évolution des tas, les actions réalisées par chaque joueur
    et le gagnant !
    
    Paramètre:
    ---------
    joueur : int
        le numéro du joueur courant
        
    Valeur renvoyée :
    ----------------    
    int 
    """
    
    nb_allumette = 20
    ordinateur = random.randint(1, 2)
    print("L'ordinateur est le joueur numéro ", ordinateur)
    separateur('#')
    affichage(nb_allumette, '*')    
    #à  compléter


""" 
Exemple de partie

L'ordinateur est le joueur numéro  2
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
20 objets restants :
* * * * * * * * * * * * * * * * * * * * 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 3
Le joueur numéro  1  enlève  3 allumettes

--------------------------------------------------------------------------------
17 objets restants :
* * * * * * * * * * * * * * * * * 
--------------------------------------------------------------------------------

Le joueur numéro  2  enlève  1 allumettes

--------------------------------------------------------------------------------
16 objets restants :
* * * * * * * * * * * * * * * * 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 2
Le joueur numéro  1  enlève  2 allumettes

--------------------------------------------------------------------------------
14 objets restants :
* * * * * * * * * * * * * * 
--------------------------------------------------------------------------------

Le joueur numéro  2  enlève  2 allumettes

--------------------------------------------------------------------------------
12 objets restants :
* * * * * * * * * * * * 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 3
Le joueur numéro  1  enlève  3 allumettes

--------------------------------------------------------------------------------
9 objets restants :
* * * * * * * * * 
--------------------------------------------------------------------------------

Le joueur numéro  2  enlève  1 allumettes

--------------------------------------------------------------------------------
8 objets restants :
* * * * * * * * 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 1
Le joueur numéro  1  enlève  1 allumettes

--------------------------------------------------------------------------------
7 objets restants :
* * * * * * * 
--------------------------------------------------------------------------------

Le joueur numéro  2  enlève  3 allumettes

--------------------------------------------------------------------------------
4 objets restants :
* * * * 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 3
Le joueur numéro  1  enlève  3 allumettes

--------------------------------------------------------------------------------
1 objets restants :
* 
--------------------------------------------------------------------------------

Le joueur numéro  2  enlève  1 allumettes

--------------------------------------------------------------------------------
0 objets restants :

--------------------------------------------------------------------------------

Joueur  2  gagnant !
"""