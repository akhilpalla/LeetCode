# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.foundP = False
        self.foundQ = False

    # Helper function to find LCA and track if p and q exist
    def findLCA(self, root, p, q):
        if root is None:
            return None

        # Recur for the left and right subtrees
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)

        # Check if current node is either p or q
        if root is p:
            self.foundP = True
            return root
        if root is q:
            self.foundQ = True
            return root

        # If p and q are found in left and right subtrees respectively, this is the LCA
        if left and right:
            return root

        # Otherwise return the non-null child (if both are null, returns None)
        return left if left else right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = self.findLCA(root, p, q)
        
        # Return LCA only if both p and q are found
        if self.foundP and self.foundQ:
            return lca
        else:
            return None
