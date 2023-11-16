# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) 
# the container can contain is 49.

import time 

height = [1,8,6,2,5,4,8,3,7]

# bekar solution hai ...
# ye to kaam bhi nahi kar raha hai..

def maxArea(height: list[int]) -> int:
    
    area = []
    for i in range(len(height)):
        for j in height:
            area.append(i*j)
    return max(area)    


# mtd 2 : pointers ko move karke left pointer fixed then right ko uske respect me move
#         karunga

# breath = diff of l and r 
# height = min of the height of the columns
    
    
def maxArea2(height: list[int]) -> int:   
    
    l = 0  
    r = len(height) - 1
    
    maxarea = 0
    
    while l< r :
        breadth = r - l 
        length = min(height[l],height[r])
        area = length*breadth
        maxarea = max(area, maxarea)
        
        if height[l] <= height[r] :
            l+=1
        else:
            r-=1
       
    return maxarea    
        
        
print(maxArea2(height))   