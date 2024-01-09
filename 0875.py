# 0875.py KOKO eating Banana



# Example 1:


# Input: piles = [3,6,7,11], h = 8
# Output: 4


# Example 2:


# Input: piles = [30,11,23,4,20], h = 5
# Output: 30


# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

from math import ceil

piles = [30,11,23,4,20]
h = 6

def minEatingSpeed(piles:list[int] , h : int) -> int:
    
    for k in range(1,max(piles)+1):
        print(f"speed-{k}")
        time = 0
        for p in piles:
            time += ceil(p/k)
        
        print(f"time-{time}")    
        if time <= h:
            return k
      
print(minEatingSpeed(piles,h))

