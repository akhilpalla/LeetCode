# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        hashset = set()

        def dfs(node, curRoot):
            if not node:
                if curRoot == 1:
                    return
                return False
            
            if (target - node.val) in hashset:
                if curRoot == 1:
                    return
                return True
            
            hashset.add(node.val)
            return dfs(node.left, curRoot) or dfs(node.right, curRoot) 
        
        dfs(root1, 1)
        return dfs(root2, 2)