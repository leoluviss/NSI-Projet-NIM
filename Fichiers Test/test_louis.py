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
