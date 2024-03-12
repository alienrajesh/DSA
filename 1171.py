# 1171. Remove Zero Sum Consecutive Nodes from Linked List
#
#
# Given the head of a linked list, we repeatedly delete consecutive sequences of
# nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any
# such answer.
# (Note that in the examples below, all sequences are serializations of ListNode
#  objects.)
#
# Example 1:
#
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
#
# Example 2:
#
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
#
# Example 3:
#
# Input: head = [1,2,3,-3,-2]
# Output: [1]
#  
# Constraints:
# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeZeroSumSublists(self, head: [ListNode]) -> [ListNode]:
        dummy = ListNode(0,head)
        prefix_sum = 0
        sum_hash = {0:dummy}
        curr = head

        while curr :
            prefix_sum += curr.val
            if prefix_sum in sum_hash:
                to_delete = sum_hash[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val

                while to_delete != curr:
                    del sum_hash[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                sum_hash[prefix_sum].next = curr.next
            else:
                sum_hash[prefix_sum] = curr
            curr = curr.next

        return dummy.next  
