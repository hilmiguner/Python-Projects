def mergeSort(arr: list):
    def merge(arr1, arr2):
        firstPointer = 0
        secondPointer = 0
        resultList = []
        while firstPointer < len(arr1) and secondPointer < len(arr2):
            if arr1[firstPointer] < arr2[secondPointer]:
                resultList.append(arr1[firstPointer])
                firstPointer += 1
            else:
                resultList.append(arr2[secondPointer])
                secondPointer += 1
        while firstPointer < len(arr1):
            resultList.append(arr1[firstPointer])
            firstPointer += 1
        while secondPointer < len(arr2):
            resultList.append(arr2[secondPointer])
            secondPointer += 1
        return resultList
    def divide(arr):
        if len(arr) == 1:
            return arr
        midPoint = int(len(arr)/2)
        leftPart = arr[:midPoint]
        rightPart = arr[midPoint:]
        return merge(divide(leftPart),divide(rightPart))
        
    return divide(arr)

liste = [31, 12, 24, 36, 48, 55, 3]
result = mergeSort(liste)
print(result)
        