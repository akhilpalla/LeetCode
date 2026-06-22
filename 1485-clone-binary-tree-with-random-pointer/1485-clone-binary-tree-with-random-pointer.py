# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        copied = {}
        copied[root] = NodeCopy(root.val)
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node.left:
                if node.left not in copied:
                    copied[node.left] = NodeCopy(node.left.val)
                    dq.append(node.left)
                copied[node].left = copied[node.left]
            if node.right:
                if node.right not in copied:
                    copied[node.right] = NodeCopy(node.right.val)
                    dq.append(node.right)
                copied[node].right = copied[node.right]
            if node.random: 
                if node.random not in copied:
                    copied[node.random] = NodeCopy(node.random.val)
                    dq.append(node.random)
                copied[node].random = copied[node.random]
        return copied[root]