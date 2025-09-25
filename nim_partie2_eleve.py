#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet 1 : jeu de Nim
Squelette de la partie 2
"""

from nim_partie1_eleve import separateur, saut_de_ligne, affichage, prochain_joueur

#%% Manipulation de tableaux

def inversion_tableau(tab):
    """
    Renvoie un tableau  avec les éléments
    de tab dans l'ordre inverse (tab[::-1])

    Parameters:
    -----------
        tab : list
            tableau d'éléments de même type

    Returns:
    --------
        tableau d'éléments du même type que tab[0]
    """
    inv_tab = []
    #à  compléter
    return inv_tab


#Tests unitaires
assert inversion_tableau([]) == []
assert inversion_tableau([1,1]) == [1,1]
assert inversion_tableau([1,5]) == [5,1]
assert inversion_tableau([1, 5, 4]) == [4, 5, 1]
assert inversion_tableau([1, -5, 4]) == [4, -5, 1]


def copie_tab(tab):
    """
    Renvoie une copie superficielle du
    tableau tab  

    Parameters:
    -----------
        tab : list
            un tableau d'éléments de type simple
            (int, float, bool)

    Returns:
    --------
        tableau d'éléments du même type que tab[0]
    """
    #à compléter



#Tests unitaires
assert copie_tab([]) == []
assert copie_tab([1,1]) == [1,1]
assert copie_tab([1, -5, 4]) == [1, -5, 4]



def tous_zeros(tab):
    """
    Détermine si un tableau de bits (0 ou 1) 
    contient uniquement des 0

    Parameters:
    -----------
        tab : list
            un tableau de bits (0 ou 1)

    Returns:
    --------
        boolean
    """
    # compléter



#Tests unitaires
assert not tous_zeros([])
assert tous_zeros([0, 0, 0])
#à compléter avec d'autres tests pertinents

#%% Numération binaire

def binaire_vers_decimale(tab):
    """
    Renvoie l'entier naturel
    dont le tableau de bits est tab

    Parameters:
    -----------
        tab : tableau de bits (0 ou 1)

    Returns:
    -------
        decimale : int
    """
    puissance = 1
    decimale = 0
    #à compléter


#tests unitaires
assert binaire_vers_decimale([0]) == 0
assert binaire_vers_decimale([1]) == 1
assert binaire_vers_decimale([1, 0]) == 2
assert binaire_vers_decimale([1, 1]) == 3
assert binaire_vers_decimale([1, 0, 0]) == 4
assert binaire_vers_decimale([1, 0, 1]) == 5

def decimale_vers_binaire(n):
    """
    Renvoie le tableau de bits
    de la représentation binaire de n
    Bits de poids forts à gauche

    Parameters:
    -----------
        n: int
            un entier >=0 en base 10
            précondition n >= 0

    Returns:
    --------
        tableau d'entiers
    """
    #précondition
    assert n >= 0
    binaire = []
    #à compléter


#tests unitaires
assert decimale_vers_binaire(0) == [0]
assert decimale_vers_binaire(1) == [1]
assert decimale_vers_binaire(2) == [1, 0]
assert decimale_vers_binaire(3) == [1, 1]
assert decimale_vers_binaire(4) == [1, 0, 0]
assert decimale_vers_binaire(5) == [1, 0, 1]


#%% Opérateur XOR

def xor(bit1, bit2):
    """
    Renvoie le bit obtenu par 
    OU EXCLUSIF de bit1 et bit2

    Parameters:
    -----------
        bit1 : int 
            un bit 0 ou 1
        bit2 : int
            un bit 0 ou 1

    Returns:
    --------
        int : 
            un bit 0 ou 1
    """
    #précondition
    assert (bit1 in [0,1]) and (bit2 in [0,1])
    #à compléter


#tests unitaires
#à compléter


def bourrage_zero_gauche(tab, n):
    """
    Remplit à gauche avec des zéros
    un tableau tab pour obtenir
    un tableau de taille n

    Args:
        tab : list
            tableau de bits
            précondition : len(tab) <= n
        n : int
            un entier naturel 
            précondition : n >= 0
    Returns:
        un tableau d'entiers de type list
    """
    #précondition
    assert (len(tab) <= n)   and (n >= 0)
    # à compléter

#tests unitaires
assert  bourrage_zero_gauche([1, 0, 1], 3) == [1, 0, 1]
assert  bourrage_zero_gauche([1, 0, 1], 4) == [0, 1, 0, 1]
assert  bourrage_zero_gauche([1, 0, 1], 5) == [0, 0, 1, 0, 1]
assert  bourrage_zero_gauche([], 3) == [0, 0, 0]



def xor_tab(tab1, tab2):
    """
    Renvoie un tableau de bits
    de longueur max(len(tab1), len(tab2))
    où chaque bit s'obtient par xor
    des bits de même place de tab1 et tab2
    On travaille sur des copies de tab1 et tab2
    et on remplit par des zéros à gauche
    le tableau de plus petite taille

    Parameters:
    -----------
        tab1 : list
            tableau de bits (0 ou 1)

        tab2 : list
            tableau de bits (0 ou 1)

    Returns:
        tableau de bits (0 ou 1)
        de type list
    """
    tab3 = copie_tab(tab1)
    tab4 = copie_tab(tab2)
    #à compléter

#tests unitaires
assert  xor_tab([1, 0, 1], [1, 1, 1]) == [0, 1, 0]
assert  xor_tab([1, 0, 1], [1,1]) == [1, 1, 0]
assert  xor_tab([1, 1], [1, 1, 1]) == [1, 0, 0]

#%% Stratégie gagnante


def affichage_tas(tas, caractere):
    """
    Affiche dans l'ordre les objets restants dans les différents
    tas contenus avec un caractere pou un objet
    Utilise la fonction affichage
    
    Paramètre:
    ---------    
    tas : tableau  d'entiers
        tab[k] est le nombre d'objets dans le tas d'index k
        
    Valeur renvoyée :
    ----------------    
    None    
    """
    for k in range(len(tas)):
        saut_de_ligne(1)    
        separateur('@')
        print("Tas numéro ", k)
        affichage(tas[k], '*')
        saut_de_ligne(1)

#à compléter (affichage)



def somme_nim(tas):
    """
    Renvoie un tableau de bits (0 ou 1), représentant
    la somme de nim des représentations binaires
    des nombres d'objets de chaque tas
    Utilise les fonctions xor_tab et decimale_vers_binaire
    
    Paramètre:
    ---------    
    tas : tableau  d'entiers
        tab[k] est le nombre d'objets dans le tas d'index k
        
    Valeur renvoyée :
    ----------------    
    tableau de bits 0 ou 1 de type list    
    """
    s = [0]
    #à compléter 
    return s


#tests unitaires
assert somme_nim([2, 2]) == [0, 0]
assert somme_nim([2, 1]) == [1, 1]
assert somme_nim([2, 3]) == [0, 1]
assert somme_nim([33, 59, 25, 3]) == [0, 0, 0, 0, 0, 0]
assert somme_nim([28, 59, 25, 3]) == [1, 1, 1, 1, 0, 1]
assert somme_nim([1, 3, 4]) == [1, 1, 0]



import random


def choix_joueur_somme_nim(tas):
    """[summary]

    Parameters:
    -----------
        tas ([type]): [description]

    Returns:
    --------
        [type]: [description]
    """
    saut_de_ligne(1)
    separateur('-')
    choix_tas = int(input("Choix du tas ? "))
    choix_objet = int(input("Nombre d'objets à retirer ? "))
    while not(0 <= choix_tas < len(tas) and    1 <= choix_objet <= tas[choix_tas]):
        print("Choix invalide")
        choix_tas = int(input("Choix du tas ? "))
        choix_objet = int(input("Nombre d'objets à retirer ? "))
    return choix_tas, choix_objet

def choix_ordinateur_somme_nim(tas):
    """[summary]

    Parameters:
    -----------
        tas ([type]): [description]

    Returns:
    --------
        [type]: [description]
    """    
    snim = somme_nim(tas)
    if not tous_zeros(snim):
        for k in range(len(tas)):
            nb_objet = tas[k]
            difference_snim = binaire_vers_decimale(xor_tab(decimale_vers_binaire(nb_objet), snim))
            if difference_snim < nb_objet:
                choix_tas = k
                choix_objet = nb_objet - difference_snim
    else:
        choix_tas = -1
        choix_objet = -1
        while not(0 <= choix_tas < len(tas) and    1 <= choix_objet <= tas[choix_tas]):
            choix_tas = random.randint(1, len(tas))
            choix_objet = random.randint(1, tas[choix_tas])
    return choix_tas, choix_objet


def partie_somme_nim(tas):    
    """
    Simule une partie de jeu de Nim classique entre un humain et 
    l'ordinateur, ce dernier applique la stratégie gagnante décrite
    dans l'énoncé.
    Affiche l'évolution des tas, les actions réalisées par chaque joueur
    et le gagnant !

    Parameters:
    -----------
        tas : list
            tableau d'entiers
            tas[k] est le nombre d'objets dans le tas d'index k
            avec 0 <= k < len(tas)

    Returns:
    --------
        None
    """    
    ordinateur = random.randint(1, 2)
    print("L'ordinateur est le joueur numéro ", ordinateur)
    separateur('#')
    affichage_tas(tas) 
    #à compléter


#à compléter (affichage d'exécution de partie_somme_nim([1, 3, 7]))