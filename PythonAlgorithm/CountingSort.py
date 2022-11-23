def CountingSort(inputArr):

    maxElem = max(inputArr)
    countingLength = maxElem + 1
    countingArr = [0] * countingLength

    for elem in inputArr:
        countingArr[elem] += 1

    for idx in range(1, countingLength):
        countingArr[idx] += countingArr[idx-1]

    outputArr = [0] * len(inputArr)

    idx = len(inputArr) - 1
    while idx >= 0:
        current = inputArr[idx]
        countingArr[current] -= 1
        newPosition = countingArr[current]
        outputArr[newPosition] = current
        idx -= 1

    return outputArr


if __name__ == "__main__":
    arr = [45,22,65,78,9,23,89,52]
    print("Original array:: ", arr)
    print("After counting sort", CountingSort(arr))