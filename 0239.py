# NEETCODE Topic - Sliding Window


# 239. Sliding Window Maximum

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


# Example 2:

# Input: nums = [1], k = 1
# Output: [1]



nums = [1,3,-1,-3,5,3,6,7]
k = 3

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []
    window = []

    for r in range(k):
        window.append(nums[r])
    # print(window)
    res.append(max(window))
    
    l = 0 
    r = k
    # there might be an edge case 
    
    while r < len(nums):
        window.append(nums[r])
        window.remove(nums[l])
        res.append(max(window))
        print(f"Window at step{l} {window}")
        l+=1
        r+=1
    return res   
        
        

     
        
print(maxSlidingWindow(nums,k))

