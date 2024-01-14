# 0033.py Search in Rotated Sorted Array

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4


# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


# Example 3:

# Input: nums = [1], target = 0
# Output: -1

# Brute force 
# Time - 
# Space - 

nums = [4,5,6,7,8,0,1,2,]
target = 8

def search(nums: list[int], target: int) -> int:
    
    l , r = 0 , len(nums)-1
    
    while l<=r :
        m = (l+r) // 2 
        if nums[m] == target :
            return m 
        

        if nums[l] == target:
            return l 
        elif nums[r] == target:
            return r 
        elif nums[m] > target and nums[l] > target:
            l = m+1
        elif nums[m] < target:
            l = m+1
        else :
            r = m -1 
    return -1


print(search(nums,target))