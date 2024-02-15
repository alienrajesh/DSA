# 0143.py Reorder Linked List
# Problem Statement :
# You are given the head of a singly linked-list.
# The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes.
# Only nodes themselves may be changed.

# Example 1 :
# head   = 1 --> 2 --> 3 --> 4 --> 5
# output = 1 --> 5 --> 2 --> 4 --> 3


# Example 2 :
# head    = 1 --> 2 --> 3 --> 4
# output  = 1 --> 4 --> 2 --> 3


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            # need to do one more time
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merging Two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        return head


class Solution1:
    def reorderList(self, head: [ListNode]) -> None:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next 

        print(head_list)

my_solution = Solution1()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
my_solution.reorderList(head)

# my_solution = Solution()
# reordered_list = my_solution.reorderList(head)

# while reordered_list:
#     suffix = " --> "

#     if not reordered_list.next:
#         suffix = ""
#     print(reordered_list.val, end=suffix)
#     reordered_list = reordered_list.next
