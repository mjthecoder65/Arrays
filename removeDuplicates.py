def removeDuplicates(nums: List[int]) -> int:
    store = set()
    index = 0
    
    for num in nums:
        if num not in store:
            store.add(num)
            nums[index] = num
            index += 1
    
    for i in range(index, len(nums)):
        nums[i] = None
    
    return index




