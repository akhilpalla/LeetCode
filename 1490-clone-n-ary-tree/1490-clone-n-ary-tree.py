"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root:
            return self.dfs(root)
    def dfs(self, node):
        _node = Node(node.val)
        if not node.children:
            return _node
        _node.children = []
        for child in node.children:
            _node.children.append(self.dfs(child))
        return _node