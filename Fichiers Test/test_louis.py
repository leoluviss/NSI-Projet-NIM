def binaire_vers_decimale(tab):
    puissance = 1
    decimale = 0
    for bit in reversed(tab):
        decimale += bit * puissance
        puissance *= 2
    return decimale

#tests unitaires
assert binaire_vers_decimale([0]) == 0
assert binaire_vers_decimale([1]) == 1
assert binaire_vers_decimale([1, 0]) == 2
assert binaire_vers_decimale([1, 1]) == 3
assert binaire_vers_decimale([1, 0, 0]) == 4
assert binaire_vers_decimale([1, 0, 1]) == 5

def decimale_vers_binaire(n):
    assert n >= 0
    binaire = []
    if n == 0:
        return [0]
    while n > 0:
        binaire.append(n % 2)
        n //= 2
    binaire.reverse()
    return binaire

#tests unitaires
assert decimale_vers_binaire(0) == [0]
assert decimale_vers_binaire(1) == [1]
assert decimale_vers_binaire(2) == [1, 0]
assert decimale_vers_binaire(3) == [1, 1]
assert decimale_vers_binaire(4) == [1, 0, 0]
assert decimale_vers_binaire(5) == [1, 0, 1]
