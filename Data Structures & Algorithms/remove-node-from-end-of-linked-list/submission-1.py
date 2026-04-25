# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Run untill pointer move n time
        # Then we'll start a new point from left
        # Till we hit end for first pointer, so that
        # lenght from end will be n
        while 0 < n:
            right = right.next
            n -= 1
    
        # Run right till end
        while right:
            left = left.next
            right = right.next
        # Now left will be at n - 1

        # Skip nth
        left.next = left.next.next
        return dummy.next