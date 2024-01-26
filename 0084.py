
# 0084.py  Largest Rectangle in  Histogram



# Example 1:

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area,
# which has an area = 10 units.


# Example 2:

# Input: heights = [2,4]
# Output: 4

heights = [2,1,5,6,2,3]

# Time  -  O(N)
# Space -  O(N)

def largestRectangleArea(heights: list[int]) -> int:
    
    maxArea = 0
    stack = [] # pair : (index,height)
    
    for i , h in enumerate(heights):
        start = i 
        
        while stack and stack[-1][1] > h:
            index , height = stack.pop()
            maxArea = max(maxArea, height*(i-index))
            start = index
        stack.append((start,h))
    
    print(stack)
        
    for i , h in stack :
        maxArea = max(maxArea , h * (len(heights)-i))
    
    return maxArea


print(largestRectangleArea(heights))
        
        
        
