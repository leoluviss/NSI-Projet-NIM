def inversion_tableau(tab):
    inv_tab = [0] * len(tab)  # Crée une liste vide avec la même taille
    for t in range(len(tab)):
        inv_tab[len(tab)-t-1] = tab[t]  # Place l'élément tab[t] à la position inversée dans inv_tab
    return inv_tab

def inversion_tableau2(tab):
    return tab[::-1]

print(inversion_tableau([1, 5, 4]))
print(inversion_tableau2([1, 5, 4]))