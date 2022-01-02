def findKthLargest(arr : list(int), k: int) ->int:
    arr = sorted(arr, reverse=True)
    if k <= len(arr):
        return arr[k-1]

# This work better if we have distinct element
def findKthLargest(arr, k):
    smallest = arr[0]
    largest = arr[0]

    store = {}
    for key in arr:
        if key in store: store[key] += 1 
        else: store[key] = 1

    for element in arr:
        if element < smallest: smallest = element
        elif element > largest: largest = element
    count = 0

    key = largest

    while (key >= smallest):
        if key in store:
            count += store[key]
            if count >= k: 
                return key
        key -= 1
# Another solution here is to use Heap

from heapq import heapify, heappop

def findKthLargest(arr, k):
    arr = [-x for x in nums]
    heapify(arr)
    kth_largest = None

    while k > 0:
        kth_largest = -heappop(arr)
        k -= 1
    return kth_largest


if __name__ == "__main__":
    arr = [3,2,3,1,2,4,5,5,6]
    result = findKthLargest(arr, 4)
    print(result)