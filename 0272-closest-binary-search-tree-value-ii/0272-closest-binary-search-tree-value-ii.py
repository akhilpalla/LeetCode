# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        h = []

        def calc(node):
            if not node:
                return

            heapq.heappush(h, (abs(node.val - target), node.val))

            calc(node.left)
            calc(node.right)

        calc(root)

        res = []
        while k:
            _, val = heapq.heappop(h)
            res.append(val)

            k -= 1

        return res
        