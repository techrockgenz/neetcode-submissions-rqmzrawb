# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Complex my sln, check next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next

        while fast:
            if fast == slow:
                return True
            slow = slow.next
            if not fast or not fast.next:
                return False
            fast = fast.next.next
        return False