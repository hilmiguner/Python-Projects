def insertionSort(arr: list):
    length = len(arr)
    for i in range(1, length):
        for k in range(i, 0, -1):
            if arr[k] < arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]
            else:
                break
    return arr

liste = [31, 12, 24, 36, 48, 55, 3]
resultList = insertionSort(liste)
print(resultList)