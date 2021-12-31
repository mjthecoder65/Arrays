# Move negative elements to the right of the array.
# The order of elements shouldn't change

def moveNegativesToEnd(arr):
    negatives = []
    positives = []
    for element in arr:
        if element > 0:
            positives.append(element)
        else:
            negatives.append(element)
    result = positives + negatives
    for i in range(len(result)):
        arr[i] = result[i]


def moveNegativesToEnd(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    arr = [1, -1, 3, 2, -7, -5, 11, 6]
    moveNegativesToEnd(arr)
    print(arr)

