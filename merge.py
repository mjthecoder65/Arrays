# def merge(nums1: list[int],m : int, nums2: list[int], n : int)-> None:
#     i = j = 0
#     result = []
#     while i < m and j < n:
#         if nums1[i] <= nums2[j]:
#             result.append(nums1[i])
#             i += 1
#         else: 
#             result.append(nums2[j])
#             j += 1

#     if i < m:
#         while i < m:
#             result.append(nums1[i])
#             i += 1
#     if j < n:
#         while j < n:
#             result.append(nums2[j])
#             j += 1

#     for i in range(len(result)):
#         nums1[i] = result[i]

#     return nums1


def merge(nums1: list[int],m : int, nums2: list[int], n : int)-> None:
    j = 0
    for i in range(m, len(nums1)):
        nums1[i] = nums2[j]
        j += 1
    nums1.sort()
    return nums1


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

    return nums1

output = merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(output)





