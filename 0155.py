
# 155. Min stack 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        if not self.stack and not self.minstack:
            self.stack.append(val)
            self.minstack.append(val)
        else:
            if self.minstack[-1] > val:
                # self.minstack.pop()
                self.minstack.append(val)
                self.stack.append(val)
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
            
    
    def __str__(self) -> str:
        return f"""The stack - {self.stack}
The minsack - {self.minstack}"""

# output :           [null,null,null,null,-2,null,0,-2]
#  expected output : [null,null,null,null,-3,null,0,-2]  
stack = MinStack()

stack.push(0)
stack.push(1)
stack.push(0)
print(stack)
print(stack.getMin())
stack.pop()
print(stack.getMin())

print(stack)


    
    