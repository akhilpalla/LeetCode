# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            nextL, nextR, root.left, root.right = root.left, root.right, None, None
            while nextL:
                nextL.left, nextL.right, root, nextL, nextR = nextR, root, nextL, nextL.left, nextL.right
        return root