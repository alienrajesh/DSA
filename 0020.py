
## 0020.py - Valid parenthesis 


# Example 1:

# Input: s = "()"
# Output: true


# Example 2:

# Input: s = "()[]{}"
# Output: true


# Example 3:

# Input: s = "(]"
# Output: false


##  letter          ascii 
#     (               40
#     )               41
#     [               91
#     ]               93
#     {               123
#     }               125
  
#  ( { [ ] } ) 
    
s = "["
    
def isValid(s:str) -> bool:
    
    stack = []
    for i in range(len(s)):
        # print(f"{s[i]}")
        if s[i] == "(" :
            stack.append(")")
        elif s[i] == "{":
            stack.append("}")
        elif s[i] == "[":
            stack.append("]")
        else: 
            if stack == []:
                return False   
            if s[i] == stack[-1]:  
                stack.pop()
            else:
                return False
        # print(f"stack : {stack}")  
    if stack != []:
        return False 
     
    return True             
        
        
 
def isValid2(s:str) -> bool:
    
    stack = []
     
    bracket = {
        ")" : "(" ,
        "]" : "[" ,
        "}" : "{" ,
    }      
            
    for c in s:
        # print(c)
        if c in bracket:
            if stack and stack[-1] == bracket[c]:
                stack.pop()
            else:
              return False
        else:
            stack.append(c) 
        # print(stack)
    
    return True if not stack else False  
                
print(isValid2(s))        


