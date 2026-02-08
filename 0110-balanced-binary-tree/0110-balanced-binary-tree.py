# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.height(root) >= 0)
    
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0  
        lh, rh = self.height(root.left), self.height(root.right)
        if lh < 0 or rh < 0 or abs(lh - rh) > 1:
            return -1
        return max(lh, rh) + 1