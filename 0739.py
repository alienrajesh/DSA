
# Daily Temperature 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]


# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]


# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 
temperatures = [73,74,75,71,69,72,76,73]




## Time - O(n^2) 
## space - O(n) 
def dailyTemperatures( temperatures: list[int]) -> list[int]:
    
    res = []
    
    for i in range(len(temperatures)):
        stack = []
        j = i 
        while j < len(temperatures): 
            
            if temperatures[j] > temperatures[i]:
                break
            else:
                stack.append(temperatures[j])
            
            j += 1
            
        if j == len(temperatures) :
            res.append(0)
        else:
            res.append(len(stack))
            
    
    return res  

print(dailyTemperatures( temperatures))




def dailyTemperatures2(temperatures:list[int]) -> list[int]:
    
    res = [0]* len(temperatures)
    stack = [] # pair : [temp,index] 
    
    for i , t in enumerate(temperatures):
        
        while stack and t > stack[-1][0]:
            stackT , stackInd = stack.pop()
            
            res[stackInd] = i - stackInd
        stack.append((t,i))

    return res

print(dailyTemperatures2(temperatures))