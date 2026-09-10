# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result=0
        def dfs(node):
            nonlocal result
            if not node:
                return 0,0
            leftSum,leftCount=dfs(node.left)
            rightSum,rightCount=dfs(node.right)
            curr_sum=node.val+leftSum+rightSum
            curr_count=1+leftCount+rightCount
            if curr_sum//curr_count==node.val:
                result+=1
            return curr_sum,curr_count
        dfs(root)
        return result 