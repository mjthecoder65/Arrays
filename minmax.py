#Approach 2
def getMinMax(arr: list[int])-> list[int]:
    if len(arr) == 0: return []
    size = len(arr)
    sortedArr = sorted(arr)
    return [sortedArr[0], sortedArr[size-1]]
    
#Approach 2
def getMinMax(arr: list[int])-> list[int]:
    minElement = arr[0]
    maxElement = arr[0]

    for i in range(len(arr)):
        if arr[i] < minElement:
            minElement = arr[i]
        if arr[i] > maxElement:
            maxElement = arr[i]
    return [minElement, maxElement]

