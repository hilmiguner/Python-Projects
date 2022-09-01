liste = [31, 12, 24, 36, 48, 55, 3]

def sequentielSearch(x:list, y:int):
    for data in x:
        if data == y:
            return True
    return False

print(sequentielSearch(liste, 12))
print(sequentielSearch(liste, 8))

