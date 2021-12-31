# Arrays Problems

# Problem 1(Peak Element)

A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.

```python
def findPeakElement(arr):
    if len(arr) == 0: return -1
    if len(arr) == 1: return 0
    for i in range(len(arr)):
        if i == len(arr) - 1:
            if arr[i] > arr[i-1]:
                return i
            else:
                return -1
        elif(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
            return i
    return -1
```
