# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def areSameTrees(p, q):
            return (
                        (not p and not q) or
                        (p != None and q != None and p.val == q.val and
                            areSameTrees(p.left, q.left) and
                            areSameTrees(p.right, q.right)
                        )
                    )

        if areSameTrees(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))