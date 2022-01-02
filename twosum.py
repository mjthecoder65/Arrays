# def getPairWithSum(nums: list[int], target):
#     compliments = {}

#     for i, num in enumerate(nums):
#         if num in compliments: 
#             return [compliments[num], i]
#         else:
#             key = target - num
#             compliments[key] = i


def getPairWithSum(nums: list[int], target: int):
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print(getPairWithSum([2,7,11,15], 9))
print(getPairWithSum([3,2,4], 6))
print(getPairWithSum([3, 3], 6))
