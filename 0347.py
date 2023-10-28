
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


nums = [1,1,1,2,2,3]
k = 2

# O(n) - time complexity 
# O(n) - space complexity
def topKFrequent(nums: list[int], k: int = None) -> list[int]:
    
    count = {}
    freq = [[] for i in range(len(nums) +1 )]
    
    for n in nums:
        count[n] = 1 + count.get( n,0)
    
    for n , c in count.items():
        freq[c].append(n)
        
    res = []
    
    for i in range(len(freq)-1, 0 ,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    
topKFrequent(nums,k) 
    