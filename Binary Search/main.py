liste = [1, 2, 3, 4, 5, 6, 7]

def binarySearch(array, data, start, end):
    if start <= end:
        mid = start + (end - start) // 2
        if array[mid] == data:
            return mid
        elif array[mid] > data:
            return binarySearch(array, data, start, mid - 1)
        else:
            return binarySearch(array, data, mid + 1, end)
    else:
        return -1

print(binarySearch(liste, 3, 0, len(liste)-1))
print(binarySearch(liste, 1, 0, len(liste)-1))
print(binarySearch(liste, 7, 0, len(liste)-1))
print(binarySearch(liste, 8, 0, len(liste)-1))
print(binarySearch(liste, -1, 0, len(liste)-1))

