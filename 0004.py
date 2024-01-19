# 0004.py Median of Two Sorted Array 



# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Brute Force 
# Time - 
# Space - 

from math import ceil

nums1 = [1,3]
nums2 = [2,4]
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums = sorted(nums1 + nums2)
    l , r = 0 , len(nums)-1
    if len(nums) % 2 == 0 :
        mid = (l+r)//2
        return (nums[mid] + nums[(mid +1)]) /2 
        # even 
    else: 
        # odd 
        mid = ceil((l+r)/2)
        return float(nums[mid])

    # print(nums)    

print(findMedianSortedArrays(nums1,nums2))