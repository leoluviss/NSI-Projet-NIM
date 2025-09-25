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
    #à compléter
    
    
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
    #à compléter

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
    #à compléter

"""
#Affichage attendu :
>>>affichage(5, '*')

--------------------------------------------------------------------------------
5 objets restants :
* * * * * 
--------------------------------------------------------------------------------

>>>affichage(0)

--------------------------------------------------------------------------------
0 objets restants :

--------------------------------------------------------------------------------
"""


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
    n = int(input("Nombre d'objets retirés ? "))
    #à compléter 
    return n

"""
Comportement attendu

>>> choix_joueur()

--------------------------------------------------------------------------------
Nombre d'objets retirés ? 4
Choisir un nombre d'objets entre 1 et 3.
Nombre d'objets retirés ? -1
Choisir un nombre d'objets entre 1 et 3.
Nombre d'objets retirés ? 3
"""

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
    #à compléter
    
#tests unitaires
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
    affichage(nb_objet, '*')
    #à compléter


"""
Exemple de déroulement de partie :


--------------------------------------------------------------------------------
20 objets restants :
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 2
Le joueur numéro  1  enlève  2  objets

--------------------------------------------------------------------------------
18 objets restants :
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 2
Le joueur numéro  2  enlève  2  objets

--------------------------------------------------------------------------------
16 objets restants :
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 3
Le joueur numéro  1  enlève  3  objets

--------------------------------------------------------------------------------
13 objets restants :
*  *  *  *  *  *  *  *  *  *  *  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 1
Le joueur numéro  2  enlève  1  objets

--------------------------------------------------------------------------------
12 objets restants :
*  *  *  *  *  *  *  *  *  *  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 2
Le joueur numéro  1  enlève  2  objets

--------------------------------------------------------------------------------
10 objets restants :
*  *  *  *  *  *  *  *  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 2
Le joueur numéro  2  enlève  2  objets

--------------------------------------------------------------------------------
8 objets restants :
*  *  *  *  *  *  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 3
Le joueur numéro  1  enlève  3  objets

--------------------------------------------------------------------------------
5 objets restants :
*  *  *  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 1
Le joueur numéro  2  enlève  1  objets

--------------------------------------------------------------------------------
4 objets restants :
*  *  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 1
Le joueur numéro  1  enlève  1  objets

--------------------------------------------------------------------------------
3 objets restants :
*  *  *  
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Nombre d'objets retirés ? 3
Le joueur numéro  2  enlève  3  objets

--------------------------------------------------------------------------------
0 objets restants :

--------------------------------------------------------------------------------

Joueur  2  gagnant !
"""


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