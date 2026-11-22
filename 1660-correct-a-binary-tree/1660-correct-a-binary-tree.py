# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        que = deque([(root, None)])
        visited = set()
        while que:
            for _ in range(len(que)):
                v, p = que.popleft()
                if not v: continue
                visited.add(v)
                if v.right in visited:
                    if p.left == v:
                        p.left = None
                    else:
                        p.right = None 
                else:
                    que.append((v.right, v))
                que.append((v.left, v))
        return root