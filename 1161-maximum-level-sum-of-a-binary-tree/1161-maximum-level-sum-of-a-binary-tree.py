# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(int)
        def dfs(node, level):
            if not node: 
                return
            levels[level] += node.val
            dfs(node.left, level + 1), dfs(node.right, level + 1)
        dfs(root, 1)
        return max(levels, key=levels.get)