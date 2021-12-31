# Arrays Problems

# Problem 1 (Peak Element)

A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.

```python
# Approach 1
# Time complexity: O(N)
# Space complexity: O(1)
def findPeakElement(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return i
    return len(arr) - 1
```

```python
# Approach 2
# Time complexity: O(logN)
# Space complexity: O(logN)
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
```

# Problem 2 (Finding minimum and maximum element in an array)

Given an array A of size N of integers.
Your task is to find the minimum and maximum elements in the array
Input:
N = 6
A[] = {3, 2, 1, 56, 10000, 167}
Output:
min = 1, max = 10000

```python
# Approach 1
# Time complexity: O(NlogN)
# Space complexity: O(N)
def getMinMax(arr: list[int])-> list[int]:
    if len(arr) == 0: return []
    size = len(arr)
    sortedArr = sorted(arr)
    return [sortedArr[0], sortedArr[size-1]]

```

```python

# Approach 2
# Time complexity: O(N)
# Space complexity: O(1)
def getMinMax(arr: list[int])-> list[int]:
    minElement = arr[0]
    maxElement = arr[0]

    for i in range(len(arr)):
        if arr[i] < minElement:
            minElement = arr[i]
        if arr[i] > maxElement:
            maxElement = arr[i]
    return [minElement, maxElement]
```
