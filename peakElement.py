def findPeakElement(arr):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    for i in range(len(arr)):
        if i == len(arr) - 1:
            if arr[i] > arr[i-1]:
                return i
            else:
                return -1
        elif(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
            return i
    return -1

if __name__ == '__main__':
    # Write your codes here.
    pass
