#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet 1 : jeu de Nim
Squelette de la partie 1 
"""

#%% Simulation d'un duel des batonnets avec deux joueurs humains
def separateur(caractere):
    """
    Affiche une chaîne de 80 caractères de séparation
    Utilise print
    
    Parameters
    ----------
    caractere : str
        caractère de la chaîne de séparation

    Returns
    -------
    None.

    """
    for loop in range(80):
        print(caractere, end="")
    print("")
    return
    
def saut_de_ligne(n):
    """
    Affiche n sauts de lignes
    saut_de_ligne(2) saute 2 lignes par ex

    Parameters
    ----------
    n : int
        nombre de sauts de lignes

    Returns
    -------
    None.

    """
    for loop in range(n):
        print("")
    return

def affichage(n, caractere):
    """
    Affiche n objets sous forme de caractere
    sur une même ligne (option end = " " de print)
    On peut utiliser des emojis, par exemple :
    https://emojipedia.org/amphora/
    
    Paramètre:
    ---------    
    n : int
        nombre d'objets à afficher
        
    caractere: str
        caractère représentant un objet
        
    Valeur renvoyée :
    ----------------    
    None    
    """
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
    """
    Demande au joueur courant le nombre d'objets
    qu'il souhaite retirer
    
    Paramètre:
    ---------
    aucun
        
    Valeur renvoyée :
    ----------------    
    int 
        le nombre d'objets choisis
        doit être compris entre 1 et 3
    """
    saut_de_ligne(1)
    separateur('-')
    n=0
    while not (1 <= n <= 3):
        n = int(input("Nombre d'objets retirés ? "))
        if n < 1 or n > 3:
            print("Choisir un nombre d'objets entre 1 et 3.")
    return n

def prochain_joueur(joueur):
    """
    Renvoie le numéro du prochain joueur
    à partir du numéro du joueur courant
    
    Paramètre:
    ---------
    joueur : int
        le numéro du joueur courant
        précondition : joueur in [1, 2]
        
    Valeur renvoyée :
    ----------------    
    int 
    """
    assert joueur == 1 or joueur == 2
    if joueur == 1:
        return 2
    else:
        return 1

assert prochain_joueur(1) == 2
assert prochain_joueur(2) == 1


#%%

def partie_fort_boyard1():
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
    None
    """
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
    # Stratégie gagnante : laisser un multiple de 4 à l'adversaire
    if nb_objet % 4 == 0:
        return 1
    else:
        return nb_objet % 4

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
    if ordinateur == 2:
        print("L'ordinateur gagne !")
    else:
        print("Joueur", prochain_joueur(ordinateur), "gagnant !")
    return
