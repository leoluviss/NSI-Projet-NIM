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
    for i in range(len(tab)-1, -1, -1):
        inv_tab.append(tab[i])
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
    copie = []
    for element in tab:
        copie.append(element)
    return copie



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
    for bit in tab:
        if bit != 0:
            return False
    return len(tab) > 0



#Tests unitaires
assert not tous_zeros([])
assert tous_zeros([0, 0, 0])
#à compléter avec d'autres tests pertinents
