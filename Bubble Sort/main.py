liste = [31, 12, 24, 36, 48, 55, 3]

length = len(liste)

def swap(x, a, b):
    temp = x[a]
    x[a] = x[b]
    x[b] = temp

def bubbleSort(x:list, y:int):
    for i in range(0, length-1):
        for k in range(0, length-i-1):
            if x[k] > x[k+1]:
                swap(x, k, k+1)
    return x

print(bubbleSort(liste, length))

