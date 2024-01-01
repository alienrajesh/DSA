
# 853.py  Car Fleet

# Example 1:


# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
# The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. 
# The fleet moves at speed 1 until it reaches target.
# Note that no other cars meet these fleets before the destination, so the answer is 3.


# Example 2:

# Input: target = 10, position = [3], speed = [3]
# Output: 1
# Explanation: There is only one car, hence there is only one fleet.



# Example 3:

# Input: target = 100, position = [0,2,4], speed = [4,2,1]
# Output: 1
# Explanation:
# The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet,
# meeting each other at 4. The fleet moves at speed 2.
# Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet,
# meeting each other at 6. The fleet moves at speed 1 until it reaches target.


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]


def carFleet(target: int,position: list[int], speed: list[int]) -> int:
    
    
    list = []
    fleet = []    
    for i in range(len(position)):
        list.append((position[i],speed[i]))
    
    list = sorted(list)
    
    for r in range(len(list) -1,-1,-1):
        fleet.append(list[r])
        
    print(fleet)
         
   

## NEETCODE solution
# time - O(nlogn) coz of sorting
# space - O(n)

def carFleet2(target:int, position : list[int] , speed: list[int]) -> int:
    
    pair = [[p,s] for p,s in zip(position,speed)]
    stack = []
    pair.sort(reverse=True) 
    print(pair)   
    for p,s in pair:
        stack.append((target-p)/s)
        
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    
    return len(stack)
    
print(carFleet2(12, [10,8,0,5,3],  [2,4,1,1,3]))