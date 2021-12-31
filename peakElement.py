

# Approach 1
def findPeakElement(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return i
    return len(arr) - 1


# Approach 2
def findPeakElement(arr : List[int]) -> int:
    left = 0
    right = len(arr) - 1
    while (left < right):
        mid = (left + right) // 2
        if (arr[mid] > arr[mid]):
            right = mid
        else:
            left = mid + 1
    return left

# Approach 3 (Recursive solution for approach 2)
def findIndex(arr, left, right):
    if (left == right): return left
    mid = (left + right) // 2
    if (arr[mid] > arr[mid + 1]):
        return findIndex(arr, left, mid)
    else:
        return findIndex(arr, mid + 1, right)

def findPeakElement(arr: List[int]) -> int:
    return findIndex(arr, 0, len(arr) - 1)

if __name__ == '__main__':
    # Write your codes here.

    nums = [1, 2, 3, 1]
    result = findPeakElement(nums)
    print(result)
    pass
