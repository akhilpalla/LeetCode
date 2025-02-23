# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def helper(pre, post):
            if not pre:
                return None
            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root
            hold =  pre[1]
            for i in range(len(post)):
                if post[i] == hold:
                    break
            count = i + 1
            root.left = helper(pre[1:count + 1], post[:count])
            root.right = helper(pre[count + 1:], post[count:len(post) - 1])
            return root
        
        return helper(preorder, postorder)