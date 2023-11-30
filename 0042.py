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
    max_r = max_r[::-1]    

    area = 0 
    for i in range(len(height)):
        trap = min(max_r[i],max_l[i]) - height[i]
        if trap < 0 :
            trap = 0 
            area += trap
        else:
            area += trap
    return area
print(trap(height))
 

# using pointers 
     
def trap2(height:list[int]) -> int:
    
    if len(height) == 0 :
        return 0
    
    l , r = 0 , len(height)-1
    

    area = 0
    max_l = height[0]
    max_r = height[len(height)-1]
    while l < r :
        
        if max_l < max_r :
            l+=1
            max_l = max(max_l, height[l]) 
            area += max_l - height[l]
            
        else : 
            r-=1
            max_r = max(max_r, height[r])
            area += max_r - height[r]
    print(area)
            
                

trap2(height)       
        


def trap3(height:list[int]) -> int:
    if len(height) == 0 :
        return 0
    
    l , r = 0 , len(height) -1
    maxleft , maxright = height[l] , height[r]
    
    water  = 0
    while l < r :
        
        if maxleft < maxright:
            l +=1
            maxleft = max(maxleft,height[l])
            water += maxleft - height[l]      
        else:
            r -= 1
            maxright = max(maxright,height[r])
            water += maxright - height[r]
    return water     
    
print(trap3(height))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    