
# leetcode 0134.py Copy Linked List with Random Pointer

# Problem Statement :
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n 
# brand new nodes, where each new node has its value set to the value of its 
# corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in 
# the copied list such that the pointers in the original list and copied list 
# represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y,
# then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer
# points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1 : 
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: [Node]) ->  [Node]:
        oldTocopy = {None:None}
        
        curr = head 
        while curr:
            copy = Node(curr.val)
            oldTocopy[curr] = copy
            curr = curr.next
        
        curr = head 
        while curr:
            copy = oldTocopy[curr]
            copy.next = oldTocopy[curr.next] 
            copy.random = oldTocopy[curr.random]
            curr = curr.next 
            
        return oldTocopy[head]
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random =  




