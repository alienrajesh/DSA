

# 150 Evaluate Reverse Polish Notation 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9



# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6


# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def evalRPN(tokens: list[str]) -> int:
    stack = []
    for i in tokens:
        if i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "-":
            a , b = stack.pop() , stack.pop()
            stack.append(b-a)
        elif i == "*":
            stack.append(stack.pop() * stack.pop())
        elif i == "/":
            a , b = stack.pop() , stack.pop() 
            stack.append(int(b / a))
        else:
            stack.append(int(i))       
    
    return stack[0]

print(evalRPN(tokens))        
