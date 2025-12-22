# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    best = 1
    def longestConsecutive(self, root):
        self.loop(root)
        return self.best

    def loop(self,root):
        if root == None:
            return [0,0]
        left = self.loop(root.left)
        right = self.loop(root.right)
        up = 1
        down = 1
        ans = [1,1]
        if root.left:
            if root.val-1 == root.left.val:
                up += left[0]
                ans[0] = left[0]+1
            elif root.val+1 == root.left.val:
                down += left[1]
                ans[1] = left[1]+1
        if root.right:
            if root.val+1 == root.right.val:
                up += right[1]
                ans[1] = max(ans[1],right[1]+1)
            elif root.val-1 == root.right.val:
                down += right[0]
                ans[0] = max(ans[0],right[0]+1)
        self.best = max(self.best,up,down)
        return ans