# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postorder(node):
            if not node:
                return 0,None
            ld, ln = postorder(node.left)
            rd, rn = postorder(node.right)
            if ld == rd:
                return ld+1,node
            elif ld > rd:
                return ld+1,ln
            else:
                return rd+1,rn
        d , n = postorder(root)
        return n