# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_product = 0
        total_sum = self.getSum(root)
        self.getSum(root, total_sum)
        return self.max_product % MOD
    def getSum(self, node, total_sum=None):
        if not node:
            return 0
        left_sum = self.getSum(node.left, total_sum)
        right_sum = self.getSum(node.right, total_sum)
        current_sum = node.val + left_sum + right_sum
        if total_sum is not None:
            self.max_product = max(
                self.max_product,
                current_sum * (total_sum - current_sum)
            )
        return current_sum