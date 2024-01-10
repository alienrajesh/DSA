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

piles = [332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]
h = 823855818

# Brute Force solution 
# time - O(n^2)
# space - O(1)

def minEatingSpeed(piles:list[int] , h : int) -> int:
    
    for k in range(1,max(piles)+1):
        print(f"speed-{k}")
        time = 0
        for p in piles:
            time += ceil(p/k)
        
        print(f"time-{time}")    
        if time <= h:
            return k



def minEatingSpeed2(piles:list[int],h:int) -> int:
    
    l , r = 1 , max(piles)
    
    while l <= r :
        speed = round((l+r)/2)
        time = 0
        for p in piles :
            time += ceil(p/speed)
        
        if time < h :
            r = speed -1 
        elif time > h:
            l = speed + 1 
        if time == h :
            return speed
    
    return "not found"

              
print(minEatingSpeed(piles,h))

