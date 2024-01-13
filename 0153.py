# 0153.py Find minimun in Rotated Sorted Array


# Example 1:


# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.


# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.


# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

nums = [4, 5, 6, 7, 0, 1, 2]


def findMin(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    if nums[0] < nums[-1]:
        return nums[0]

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return nums[i + 1]


def findMin2(nums: list[int]):
    print(nums)
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        print(f"l-{l} , r - {r}")
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        m = (l + r) // 2
        print(f"res - {res}, nums m- {nums[m]} , {m}")
        res = min(res, nums[m])

        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

    return res


print(findMin2(nums))
