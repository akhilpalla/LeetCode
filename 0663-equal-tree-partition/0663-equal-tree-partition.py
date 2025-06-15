# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def get_sum(root, d):
            if not root:
                return 0
            l = get_sum(root.left, d)
            r = get_sum(root.right, d)
            sum = l+r+root.val
            d[sum] = d.get(sum, 0) + 1
            return sum
        d = {}
        total_sum = get_sum(root, d)
        if total_sum == 0:
            return d[0] >= 2
        return True if total_sum//2 in d and total_sum%2 == 0 else False