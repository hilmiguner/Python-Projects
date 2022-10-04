def quickSort(arr):
    def pivot(arr, pivotIx, endIx):
        swapIx = pivotIx
        firstMaxIx = 0
        for i in range(pivotIx+1, endIx+1):
            if arr[i] < arr[pivotIx]:
                swapIx += 1
                arr[i], arr[swapIx] = arr[swapIx], arr[i]
        arr[pivotIx], arr[swapIx] = arr[swapIx], arr[pivotIx]
        return swapIx

    def sort(arr, leftPointer = 0, rightPointer = None):
        if rightPointer is None:
            rightPointer = len(arr) - 1
        if leftPointer < rightPointer:
            pivotIx = pivot(arr, leftPointer, rightPointer)
            sort(arr, leftPointer, pivotIx-1)
            sort(arr, pivotIx+1, rightPointer)
        return arr

    return sort(arr)

liste = [31, 12, 24, 36, 48, 55, 3]
resultList = quickSort(liste)
print(resultList)