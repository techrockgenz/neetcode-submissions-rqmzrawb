# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Give reason that why start with infs
# If we start with brute force, then we have to not just compare
# with parent, but till root, as we can see in case of 4 - 7.
# So it'll be n^2, to avoid this we use infs.
# Root can be any value between -inf to inf, so start like this.

#   5
# 3     7
#     4   8

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(float("-inf"), root, float("inf"))])    

        while queue:
            left, node, right = queue.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                # Borrowing right from parent/root and left will be fixed -inf
                queue.append((left, node.left, node.val))
            if node.right:
                # Borrowing left from parent/root and right will be fixed inf
                queue.append((node.val, node.right, right))
        
        return True