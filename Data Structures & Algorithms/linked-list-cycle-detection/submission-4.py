# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Hashset n n
# Floyd's Tortoise & Hare n 1
# Following is not necessarily be the cycle point
# it can be anything, distance from that node to cycle is
# always distance of cycle from head

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: 
                return True
        return False