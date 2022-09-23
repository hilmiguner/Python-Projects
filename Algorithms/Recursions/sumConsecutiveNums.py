def calculateConsecutiveNums(startNum: int) -> int:
    if startNum == 1:
        return 1
    return startNum + calculateConsecutiveNums(startNum-1)

print(calculateConsecutiveNums(15))