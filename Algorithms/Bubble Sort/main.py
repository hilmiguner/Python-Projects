liste = [31, 12, 24, 36, 48, 55, 3]

length = len(liste)

def bubbleSort(x:list, y:int):
    for i in range(0, length-1):
        for k in range(0, length-i-1):
            if x[k] > x[k+1]:
                x[k], x[k+1] = x[k+1], x[k]
    return x

print(bubbleSort(liste, length))

