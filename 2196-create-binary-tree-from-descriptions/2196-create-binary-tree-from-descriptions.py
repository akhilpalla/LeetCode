# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parents = set([x[0] for x in descriptions])
        nodes = {}

        for parent,child,isLeft in descriptions:
            parents.discard(child)
            
            if not nodes.get(parent):
                nodes[parent] = TreeNode(parent)
            
            if not nodes.get(child):
                nodes[child] = TreeNode(child)

            if isLeft:
                nodes[parent].left = nodes[child] 
            else:
                nodes[parent].right = nodes[child] 
        
        return nodes[parents.pop()]