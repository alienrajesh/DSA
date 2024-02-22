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
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        
        added = ListNode(0,None)
        up = l1
        down = l2 
        
        while up and down:
            pass 
        