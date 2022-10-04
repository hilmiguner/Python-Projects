def selectionSort(arr: list):
    length = len(arr)

    for i in range(length):
        minIx = i
        for k in range(i, length):
            if arr[k] < arr[minIx]:
                minIx = k
        arr[i], arr[minIx] = arr[minIx], arr[i]
    return arr

liste = [31, 12, 24, 36, 48, 55, 3]
resultList = selectionSort(liste)
print(resultList)