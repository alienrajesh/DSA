# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is
# represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.

height = [0,1,0,2,1,0,1,3,2,1,2,1]

# formula = min(l,r) - h[i] = units of trapped water
# if trapped water = -ve then no water trapped
# else water water trapped = units in +ve 

def trap(height: list[int]) -> int:
    
    max_l = []
    max_i = 0
    for i in range(len(height)):
        max_l.append(max_i)
        max_i = max(max_i,height[i])
    
    max_r = []
    max_i = 0
    for i in range(len(height)-1,-1,-1):
        max_r.append(max_i)
        max_i= max(max_i,height[i])
    print(max_l)    
    print(reversed(max_r))    
    
      


print(trap(height))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    