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

```
Input:
N = 6
A[] = {3, 2, 1, 56, 10000, 167}
Output:
min = 1, max = 10000
```

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

# Problem 3 (Move zeros to the end of the array)

Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

```
Example 1
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2
Input: nums = [0]
Output: [0]

```

```python
 # Approach 1
 # Time complexity: O(N),
 # Space complexity : O(N)
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

```

```python
 # Approach 2
 # Time complexity: O(N),
 # Space complexity : O(1)

def moveZeroes(arr: List[int]):
    nonzerosIndex = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[nonzerosIndex] = arr[i]
            nonzerosIndex += 1
    for i in range(nonzerosIndex, len(arr)):
        arr[i] = 0
```

```python
 # Approach 3
 # Time complexity: O(N),
 # Space complexity : O(1)

def moveZeroes(arr : list(int)):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
```

# Problem 4 (Move all negative elements to the right)

Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive element and negative element.

```

Example 1
Input :
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output :
1  3  2  11  6  -1  -7  -5

Example 2
Input :
N=8
arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output :
7  9  10  11  -5  -3  -4  -1

```

```python
# Approach 1
# Time complexity: O(N)
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
```

```python
# Approach 1
# Time complexity: O(N)
# Space complexity: O(1)
def moveZeroes(arr: List[int]):
    nonzerosIndex = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[nonzerosIndex] = arr[i]
            nonzerosIndex += 1
    for i in range(nonzerosIndex, len(arr)):
        arr[i] = 0
```

# Problem 5 (Kth smallet element in array)

Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

```
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given
array is 7
```

```python
# Approach 1
# Time complexity : O(nlogn)
def kthSmallest(arr: list(int), k : int):
    arr = sorted(arr)
    if k <= len(arr):
        return arr[k - 1]
```

```python
# Approach 2
# Time complexity : O(nlogn)
def kthSmallest(arr, k):
    smallest = arr[0]
    largest = arr[0]

    store = {}
    for key in arr:
        if key in store: store[key] += 1
        else: store[key] = 1

    for element in arr:
        if element < smallest: smallest = element
        elif element > largest: largest = element

    count = 1
    for element in range(smallest, largest):
        if element in store:
            if count == k: return element
            else: count += store[element]
```

# Problem 6 (Two sum problem)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

```
Example 1

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3
Input: nums = [3,3], target = 6
Output: [0,1]

```

```python
# Approach 1 (Brute force)
# Time complexity: O(n^2)
# Space complexity: O(1)

def getPairWithSum(nums: list[int], target: int):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Approach 2
# Time Complexity: O(N)
# Space complexity: O(N)

def getPairWithSum(nums: list[int], target):
    compliments = {}

    for i, num in enumerate(nums):
        if num in compliments:
            return [compliments[num], i]
        else:
            key = target - num
            compliments[key] = i

```

# Problem 7 (merge two sorted arrays)

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

```
Example 1
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

```

```python
# Approach 1
# Time complexity : O(nlogn)
# Space complexity : O(n)

def merge(nums1: list[int],m : int, nums2: list[int], n : int)-> None:
    j = 0
    for i in range(m, len(nums1)):
        nums1[i] = nums2[j]
        j += 1
    nums1.sort()
    return nums1

#Approach 2
# Time complexity: O(n)
# Space complexity: O(1)
def merge(nums1: list[int],m : int, nums2: list[int], n : int)-> None:
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

    while i >= 0:
        nums1[k] = nums1[i]
        k -= 1
        i -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
```
