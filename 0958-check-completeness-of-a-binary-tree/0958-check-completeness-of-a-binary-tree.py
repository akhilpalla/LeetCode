# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        q = deque([(root)])
        while q[0]:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                else:
                    return not any(q)
        return not any(q)