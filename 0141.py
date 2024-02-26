# leetcode 0141.py "Linked List has Cycle"


# Given head, the head of a linked list, determine if
# the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in
# the list that can be reached again by continuously following
# the next pointer. Internally, pos is used to denote the index
# of the node that tail's next pointer is connected to. Note that
# pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list.
# Otherwise, return false.

# Example 1:
#  3 -> 2 -> 0 -> 4 
#      ^          |
#      |__________|

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation:There is a cycle in the linked list, where the tail 
#             connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail 
#             connects to the 1st node (0-indexed).


# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle( head:[ListNode]) -> bool:
        # Time - O(n) Space - O(1)
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast :
            return True
    
    return False
        

def hasCycle2(head:[ListNode]) -> bool:
    # Time - O(n) Space - O(n)
    visited = []
    curr = head 

    while curr:
        if curr in visited:
            return True
        
        visited.append(curr)

    return False


# Helper function to create a linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:  # Create cycle if pos is not -1
        nodes[-1].next = nodes[pos]
    return nodes[0]

# Helper function to print the outcome
def print_cycle_detection(values, pos):
    head = create_linked_list_with_cycle(values, pos)
    has_cycle = hasCycle(head)
    if has_cycle:
        print("Linked list with cycle:", values)
        print("Cycle detected!")
    else:
        print("Linked list without cycle:", values)
        print("No cycle detected.")

# Test cases
print_cycle_detection([1, 2, 3, 4, 5], -1)  # No cycle
print_cycle_detection([1, 2, 3, 4, 5], 1)   # With cycle
