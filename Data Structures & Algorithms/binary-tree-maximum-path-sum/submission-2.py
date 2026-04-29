# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# n, h
# max(left, right, 0) left and right could be -ve, so zero

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            if not root:
                return 0
            
            # leftMax = dfs(root.left)
            # rightMax = dfs(root.right)
            # leftMax = max(leftMax, 0)
            # rightMax = max(rightMax, 0)
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
            nonlocal res
            res = max(res, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax) # Crux, while calculating consider both left and right
            # But while return return only max of them. Also maintian max in res a global var 
        
        dfs(root)
        return res