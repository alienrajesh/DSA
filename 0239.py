# NEETCODE Topic - Sliding Window

from collections import deque
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
        if nums[r] > res[l] :
            res.append(nums[r])
        else:
            res.append(max(window))
        print(f"Window at step{l} {window}")
        l+=1
        r+=1
    return res   
    
print(maxSlidingWindow(nums,k))


## new approach this might take less time
# instead of checking the window everytime we can check the new element added is
# greater than the max of the current window 




## Neetcode solution 
# time - O(n) 
# space - O(n)

def maxSlidingWindow(nums:list[int],k:int) -> list[int]:
    res = []
    q = deque()
    l = r = 0
    while r < len(nums) :
        # pop smaller values from q 
        while q and nums[q[-1]] < nums[r] :
            q.pop()
        q.append(r)
        
        # remove left val from window 
        if l > q[0] :
            q.popleft()
        
        if (r+1) >= k:
            res.append(nums[q[0]])
            l+=1
        r +=1
    
    return res
    