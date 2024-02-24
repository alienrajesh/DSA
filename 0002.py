# leetcode 0002.py Add number two Linked List

# Problem statement 
# You are given two non-empty linked lists representing 
# two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers
# and raeturn the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except 
# the number 0 itself.

# Example 1 : 
# List1 = 2 --> 4 --> 3 
# List2 = 5 --> 6 --> 4
# Output = 7 --> 0 --> 8 
# Explaination --> 243 + 564 = 807

# Example 2 :
# List1 = 9 --> 9 --> 9 --> 9 --> 9 --> 9 --> 9 --> 9  
# List2 = 9 --> 9 --> 9 --> 9 
# Output = 8 --> 9 --> 9 --> 9 --> 0 --> 0 --> 0 --> 1 

# Example 3 : 
# List1 = 0
# List2 = 0 
# output = 0

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
   def __init__(self) :
        self.head = None

   def insert(self,data) :
        node = ListNode(data,self.head)
        self.head = node

   def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        
        number1 = ""
        number2 = ""

        while l1 :
            number1 += str(l1.val)
            l1 = l1.next 
            
        while l2 :
            number2 += str(l2.val)
            l2 = l2.next
        
        number1 = number1[::-1]
        number2 = number2[::-1]

        result = int(number2) + int(number1)

        for r in str(result):
            self.insert(int(r))
            
        return node 
# class LinkedList:

l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
my_solution = Solution()
added_numbers = my_solution.addTwoNumbers(l1,l2)

while added_numbers:
    suffix = " --> "
    if not added_numbers.next:
        suffix = ""

    print(added_numbers.val,end = suffix)
    added_numbers = added_numbers.next

