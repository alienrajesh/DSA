# 2816. Double a Number Represented as a Linked List
#
#
# You are given the head of a non-empty linked list representing a non-negative
# integer without leading zeroes.
# Return the head of the linked list after doubling it.
#
# Example 1:
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which
# represents the number 189. Hence, the returned linked list represents the
# number 189 * 2 = 378.
#
#
# Example 2:
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which
# represents the number 999. Hence, the returned linked list reprersents the
# number 999 * 2 = 1998.
#
#
# Constraints:
# The number of nodes in the list is in the range [1, 104]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not
# have leading zeros, except the number 0 itself.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # current_node = head
        # previous_node = None

        # while current_node:

        #     doubled_value = current_node.val * 2

        #     if doubled_value < 10:
        #         current_node.val = doubled_value
        #     elif previous_node:
        #         current_node.val = doubled_value % 10
        #         previous_node.val += 1
        #     else:
        #         head = ListNode(1, current_node)
        #         current_node.val = doubled_value % 10

        #     previous_node = current_node
        #     current_node = current_node.next

        # return head

        prev = None
        if head.val >= 5:
            head = ListNode(0, head)

        prev = head
        curr = head

        while curr:
            if curr.val >= 5:
                prev.val += 1
                curr.val = curr.val * 2 - 10
            else:
                curr.val *= 2

            prev = curr
            curr = curr.next

        return head
