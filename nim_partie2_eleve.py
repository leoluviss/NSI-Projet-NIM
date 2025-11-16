#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet 1 : jeu de Nim
Squelette de la partie 2
"""

from nim_partie1_eleve import separateur, saut_de_ligne, affichage, prochain_joueur

#%% Manipulation de tableaux

def inversion_tableau(tab):
    return tab[::-1]


#Tests unitaires
assert inversion_tableau([]) == []
assert inversion_tableau([1,1]) == [1,1]
assert inversion_tableau([1,5]) == [5,1]
assert inversion_tableau([1, 5, 4]) == [4, 5, 1]
assert inversion_tableau([1, -5, 4]) == [4, -5, 1]


def copie_tab(tab):
    copie_tab = [0] * len(tab)  # Crée une liste vide avec la même taille
    for t in range(len(tab)):
        copie_tab[t] = tab[t]
    return copie_tab


#Tests unitaires
assert copie_tab([]) == []
assert copie_tab([1,1]) == [1,1]
assert copie_tab([1, -5, 4]) == [1, -5, 4]


def tous_zeros(tab):
    trueorfalse=True
    if not tab:  # Vérifie si la liste est vide
        trueorfalse=False
    for t in tab:
        if t!=0:
            trueorfalse=False
    return trueorfalse

#Tests unitaires
assert not tous_zeros([])          # liste vide == False
assert tous_zeros([0, 0, 0])       # que des zéros == True
assert not tous_zeros([0, 1, 0])   # contient un non-zéro == False
assert not tous_zeros([1, 2, 3])   # que des non-zéros == False

#%% Numération binaire

def binaire_vers_decimale(tab):
    puissance = 0
    decimale = 0
    reversedtab = inversion_tableau(tab)  # On inverse le tableau pour traiter du bit de poids faible au bit de poids fort
    for bit in reversedtab:
        if bit not in (0, 1):  # Si on trouve un élément qui n'est pas 0 ou 1 dans le tableau
            assert False, "Le tableau doit contenir uniquement des 0 et des 1"  # Déclenche une erreur si un élément du tableau n'est pas un bit (0 ou 1)
        decimale += bit * (2**puissance)
        puissance += 1
    return decimale

#tests unitaires
assert binaire_vers_decimale([0]) == 0
assert binaire_vers_decimale([1]) == 1
assert binaire_vers_decimale([1, 0]) == 2
assert binaire_vers_decimale([1, 1]) == 3
assert binaire_vers_decimale([1, 0, 0]) == 4
assert binaire_vers_decimale([1, 0, 1]) == 5

def decimale_vers_binaire(n):
    assert n >= 0  # Précondition
    binaire = [None] * 32  # on réserve 32 bits
    postab = 0  # Position dans le tableau
    if n == 0:  # Cas particulier
        return [0]
    while n > 0:
        binaire[postab] = n % 2
        n = n // 2
        postab += 1
    binaire = binaire[:postab]  # On ne garde que la partie utile
    return inversion_tableau(binaire)


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
    return (bit1 + bit2) % 2


#tests unitaires
assert  xor(0, 0) == 0
assert  xor(0, 1) == 1
assert  xor(1, 0) == 1
assert  xor(1, 1) == 0

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
    if len(tab) < n:
        nb_zero = n - len(tab)
        tab_bourre = [0] * nb_zero + tab
        return tab_bourre
    else:
        return tab

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
    if len(tab3) < len(tab4):
        tab3 = bourrage_zero_gauche(tab3, len(tab4))
    elif len(tab4) < len(tab3):
        tab4 = bourrage_zero_gauche(tab4, len(tab3))
    tabxor = [0] * len(tab3)
    for i in range(len(tab3)):
        tabxor[i] = xor(tab3[i], tab4[i])
    return tabxor

#tests unitaires
assert  xor_tab([1, 0, 1], [1, 1, 1]) == [0, 1, 0]
assert  xor_tab([1, 0, 1], [1,1]) == [1, 1, 0]
assert  xor_tab([1, 1], [1, 1, 1]) == [1, 0, 0]

#%% Stratégie gagnante

import random


def affichage_tas(tas, caractere):
    """
    Affiche chaque tas avec un caractère pour représenter chaque objet.
    """
    for k in range(len(tas)):
        saut_de_ligne(1)
        separateur('@')
        print("Tas numéro", k)
        affichage(tas[k], caractere)
        saut_de_ligne(1)


def somme_nim(tas):
    """
    Renvoie la somme de Nim sous forme de tableau de bits.
    Calcule le XOR binaire de tous les tas.
    """
    s = [0]  # somme initiale = 0

    for nb in tas:
        bits = decimale_vers_binaire(nb)

        # Alignement des longueurs
        if len(bits) > len(s):
            s = bourrage_zero_gauche(s, len(bits))
        else:
            bits = bourrage_zero_gauche(bits, len(s))

        # XOR
        s = xor_tab(s, bits)

    return s


# Tests unitaires fournis
assert somme_nim([2, 2]) == [0, 0]
assert somme_nim([2, 1]) == [1, 1]
assert somme_nim([2, 3]) == [0, 1]
assert somme_nim([33, 59, 25, 3]) == [0, 0, 0, 0, 0, 0]
assert somme_nim([28, 59, 25, 3]) == [1, 1, 1, 1, 0, 1]
assert somme_nim([1, 3, 4]) == [1, 1, 0]


def choix_joueur_somme_nim(tas):
    """
    Demande à l'utilisateur de choisir un tas et combien retirer.
    Vérifie la validité des choix.
    """
    saut_de_ligne(1)
    separateur('-')
    choix_tas = int(input("Choix du tas ? "))
    choix_objet = int(input("Nombre d'objets à retirer ? "))

    while not (0 <= choix_tas < len(tas) and 1 <= choix_objet <= tas[choix_tas]):
        print("Choix invalide.")
        choix_tas = int(input("Choix du tas ? "))
        choix_objet = int(input("Nombre d'objets à retirer ? "))

    return choix_tas, choix_objet


def choix_ordinateur_somme_nim(tas):
    """
    L'ordinateur choisit le bon tas et le bon nombre d'objets à enlever
    pour mettre la somme de Nim à 0 (stratégie gagnante).
    Si la somme est déjà nulle, il joue aléatoirement.
    """
    snim = somme_nim(tas)

    if not tous_zeros(snim):
        # Position gagnante : l'ordinateur applique la stratégie
        for k in range(len(tas)):
            nb_objet = tas[k]
            difference_snim = binaire_vers_decimale(
                xor_tab(decimale_vers_binaire(nb_objet), snim)
            )
            if difference_snim < nb_objet:
                choix_tas = k
                choix_objet = nb_objet - difference_snim
                return choix_tas, choix_objet

    # Position perdante : coup aléatoire
    choix_tas = -1
    choix_objet = -1
    while not (0 <= choix_tas < len(tas) and 1 <= choix_objet <= tas[choix_tas]):
        choix_tas = random.randint(0, len(tas) - 1)
        choix_objet = random.randint(1, tas[choix_tas])
    return choix_tas, choix_objet


def partie_somme_nim(tas):
    """
    Simule une partie de Nim classique entre un humain et l'ordinateur.
    L'ordinateur applique la stratégie de Nim-sum.
    Affiche les actions et le gagnant.
    """
    ordinateur = random.randint(1, 2)
    print("L'ordinateur est le joueur numéro", ordinateur)
    separateur('#')
    affichage_tas(tas, '*')

    joueur = 1  # joueur humain = 1

    while not tous_zeros(tas):
        print("\n----------------------------------------")
        print("Au tour du joueur", joueur)
        affichage_tas(tas, '*')

        if joueur == ordinateur:
            print("L'ordinateur réfléchit…")
            choix_tas, choix_objet = choix_ordinateur_somme_nim(tas)
            print("→ L'ordinateur retire", choix_objet, "objet(s) du tas", choix_tas)
        else:
            choix_tas, choix_objet = choix_joueur_somme_nim(tas)
            print("→ Vous retirez", choix_objet, "objet(s) du tas", choix_tas)

        # Mise à jour du tas choisi
        tas[choix_tas] -= choix_objet

        # Condition de victoire
        if tous_zeros(tas):
            print("\n=== FIN DE PARTIE ===")
            if joueur == ordinateur:
                print("L'ordinateur a gagné !")
            else:
                print("Vous avez gagné !")
            return

        # Joueur suivant
        joueur = 1 if joueur == 2 else 2


# --------------------------------------------------------------
# Exemple d'exécution
# --------------------------------------------------------------

"""
Exemple d'exécution : partie_somme_nim([1, 3, 7])

L'ordinateur est le joueur numéro 2
########################################

Tas numéro 0
1 objets restants :
*

Tas numéro 1
3 objets restants :
* * *

Tas numéro 2
7 objets restants :
* * * * * * *

----------------------------------------
Au tour du joueur 1
...
"""