# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Naive: Store Inorder and search
# Better: Store inorder and do binary search
# Better2: while doing the inorder return the first value greater than 8
#Optimal: same as floor and ceil logic
class Solution:
    def __init__(self):
        self.successor = None

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        successor = None

        while(root != None):
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor