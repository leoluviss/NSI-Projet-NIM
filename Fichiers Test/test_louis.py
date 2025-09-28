def separateur(caractere):
    for loop in range(80):
        print(caractere, end="")
    print("\n")
    return
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
    for loop in range(n):
        print("")
    return
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
    for loop in range(n):
        print(caractere, end=" ")
    return
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
    n=0
    while not (1 <= n <= 3):
        n = int(input("Nombre d'objets retirés ? "))
        if n < 1 or n > 3:
            print("Choisir un nombre d'objets entre 1 et 3.")
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
    assert joueur == 1 or joueur == 2
    if joueur == 1:
        return 2
    else:
        return 1
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

print(prochain_joueur(3))
