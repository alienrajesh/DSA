

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


nums = [1,1,1,2,2,3]


def topKFrequent(nums: list[int], k: int = None) -> list[int]:
    
    hashMap = {}
    for t in nums:
        hashMap[t] = 1 + hashMap.get(t,0)
    print(hashMap)   
    
topKFrequent(nums) 
    