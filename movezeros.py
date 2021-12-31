#Approach 1
# Time complexity : O(N)
# Space complexity: O(N)

def moveZeroes(arr: List[int]):
    zeros = []
    nonzeros = []

    for element in arr:
        if element == 0:
            zeros.append(element)
        else:
            nonzeros.append(element)
    result = nonzeros + zeros
    for i in range(len(arr)):
        arr[i] = result[i]

def moveZeroes(arr: List[int]):
    nonzerosIndex = 0
    for i in range(len(arr)):
        if arr[i] != 0: 
            arr[nonzerosIndex] = arr[i]
            nonzerosIndex += 1
    for i in range(nonzerosIndex, len(arr)):
        arr[i] = 0


def moveZeroes(arr : list(int)):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
