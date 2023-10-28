
# def twoSum(nums:[int], target: int) -> [int]:
#     for a in range(len(nums)):
#         for b in range(len(nums)):
#             if a==b:
#                 continue
#             elif nums[a]+nums[b] == target:
#                 return [a,b]
#     return []       


#       
def twoSum(nums:[int], target: int) -> [int]:
    prevMap = {}
    diff = 0 
    for i , n in enumerate(nums):
        print(diff ," -> " ,prevMap)
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff] , i]
        prevMap[n] = i 
    return []
        
   



   

print(twoSum(nums = [3,4,3] , target = 6 ))