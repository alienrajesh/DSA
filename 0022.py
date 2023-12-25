
# Generate Parenthesis


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

def generateParenthesis(n: int) -> list[str]:
    
    
    stack = []
    res = []
    
    def backtrack(openN,closeN):
        if openN == closeN == n:
            res.append("".join(stack))
            return 
            
        if openN < n:
            stack.append("(")
            backtrack(openN +1,closeN)
            stack.pop()
        
        if closeN < openN:
            stack.append(")")
            backtrack(openN , closeN +1)
            stack.pop()
            
    backtrack(0,0)
    
    return res

n = 3

print(generateParenthesis(n))
