liste = [31, 12, 24, 36, 48, 55, 3]

def sequentielSearch(x:list, y:int):
    for i in range(0, len(x)):
        if x[i] == y:
            return True
    return False

print(sequentielSearch(liste, 12))
print(sequentielSearch(liste, 8))

