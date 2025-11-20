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
    return tab[::-1]


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
    copie_tab = [0] * len(tab)  # Crée une liste vide avec la même taille
    for t in range(len(tab)):
        copie_tab[t] = tab[t]
    return copie_tab


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
    return inversion_tableau(binaire) # On inverse les bits pour les remettre dans le bon sens avec la fonction inversion_tableau()


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
        print("Tas numéro", k)
        affichage(tas[k], caractere)
        saut_de_ligne(1)


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



import random


def choix_joueur_somme_nim(tas):
    """
    Permet au joueur de choisir un tas et le nombre d'objets à retirer.

    Parameters
    ----------
    tas : list[int]
        Liste des tailles des tas dans le jeu de Nim.

    Returns
    -------
    tuple[int, int]
        Un tuple contenant :
        - choix_tas : int
            L'indice du tas choisi par le joueur.
        - choix_objet : int
            Le nombre d'objets à retirer du tas choisi.
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
    Détermine le coup de l'ordinateur en fonction de la stratégie optimale du jeu de Nim.
    Si la position est gagnante (somme Nim non nulle), l'ordinateur applique la stratégie
    pour forcer une position perdante pour l'adversaire. Sinon, il choisit un coup aléatoire.

    Parameters
    ----------
    tas : list[int]
        Liste des tailles des tas dans le jeu de Nim.

    Returns
    -------
    tuple[int, int]
        Un tuple contenant :
        - choix_tas : int
            L'indice du tas choisi par l'ordinateur.
        - choix_objet : int
            Le nombre d'objets à retirer du tas choisi.
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
    print("L'ordinateur est le joueur numéro", ordinateur)
    separateur('#')
    affichage_tas(tas, '*')

    joueur = 1

    while not tous_zeros(tas):
        affichage_tas(tas, '*')

        if joueur == ordinateur:
            print("\n----------------------------------------")
            print("Au tour du joueur", joueur)
            choix_tas, choix_objet = choix_ordinateur_somme_nim(tas)
            print("L'ordinateur retire", choix_objet, "objet(s) du tas", choix_tas)
        else:
            print("\n----------------------------------------")
            print("Au tour du joueur", joueur)
            choix_tas, choix_objet = choix_joueur_somme_nim(tas)
            print("Vous retirez", choix_objet, "objet(s) du tas", choix_tas)

        tas[choix_tas] -= choix_objet   # Mise à jour du tas choisi

        # Condition de victoire
        if tous_zeros(tas):
            print("\nFIN DE PARTIE")
            if joueur == ordinateur:
                print("L'ordinateur a gagné !")
            else:
                print("Vous avez gagné !")
            return

        joueur = prochain_joueur(joueur)    # Joueur suivant
"""
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
Choix du tas ? 2
Nombre d'objets à retirer ? 3
Vous retirez 3 objet(s) du tas 2

Tas numéro 0
1 objets restants :
*
Tas numéro 1
3 objets restants :
* * *
Tas numéro 2
4 objets restants :
* * * *

----------------------------------------
Au tour du joueur 2
L'ordinateur retire 1 objet(s) du tas 1

Tas numéro 0
1 objets restants :
*
Tas numéro 1
2 objets restants :
* *
Tas numéro 2
4 objets restants :
* * * *

----------------------------------------
Au tour du joueur 1
Choix du tas ? 2
Nombre d'objets à retirer ? 2
Vous retirez 2 objet(s) du tas 2

Tas numéro 0
1 objets restants :
*
Tas numéro 1
2 objets restants :
* *
Tas numéro 2
2 objets restants :
* *

----------------------------------------
Au tour du joueur 2
L'ordinateur retire 1 objet(s) du tas 0

Tas numéro 0
0 objets restants :

Tas numéro 1
2 objets restants :
* *
Tas numéro 2
2 objets restants :
* *

----------------------------------------
Au tour du joueur 1
Choix du tas ? 1
Nombre d'objets à retirer ? 1
Vous retirez 1 objet(s) du tas 1

Tas numéro 0
0 objets restants :

Tas numéro 1
1 objets restants :
*
Tas numéro 2
2 objets restants :
* *

----------------------------------------
Au tour du joueur 2
L'ordinateur retire 2 objet(s) du tas 2

Tas numéro 0
0 objets restants :

Tas numéro 1
1 objets restants :
*
Tas numéro 2
0 objets restants :

----------------------------------------
Au tour du joueur 1
Choix du tas ? 1
Nombre d'objets à retirer ? 1
Vous retirez 1 objet(s) du tas 1

FIN DE PARTIE
Vous avez gagné !
"""