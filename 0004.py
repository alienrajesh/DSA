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
# Time - O(nlogn)
# Space - O(n)

from math import ceil

nums1 = [1,2]
nums2 = [3,4]

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums = sorted(nums1 + nums2)
    l , r = 0 , len(nums)-1
        
    # even 
    if len(nums) % 2 == 0 :
        mid = (l+r)//2
        return (nums[mid] + nums[(mid +1)]) /2 
    # odd 
    else: 
        mid = ceil((l+r)/2)
        return float(nums[mid])


# Time  - O(log(m+n))
# Space - 

def findMedianSortedArrays2(nums1: list[int], nums2: list[int]) -> float:

    A , B = nums1 , nums2
    total = len(nums1) + len(nums2)
    half = total//2 
    
    #keeping A small 
    if len(B) < len(A):
        A , B = B , A
    
    l , r = 0 , len(A) -1
    
    while True:
        
        i = (l+r) // 2 # A 
        j = half - i - 2
        
        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i+1] if (i+1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j+1] if (j+1) < len(B) else float("infinity")

        # partition is correct 
        if Aleft <= Bright and Bleft <= Aright:
            # odd 
            if total % 2 :
                return min(Aright,Bright)
            #even 
            return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
        elif Aleft > Bright :
            r = i -1
        else:
            l = i +1


print(findMedianSortedArrays2(nums1,nums2))