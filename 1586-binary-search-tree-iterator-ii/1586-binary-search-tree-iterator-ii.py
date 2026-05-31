# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = [-1]
        self.cur = 0
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.inorder.append(root.val)
            dfs(root.right)
        dfs(root)
        

    def hasNext(self) -> bool:
        return self.cur < len(self.inorder) - 1
        
    def next(self) -> int:
        self.cur+=1
        return self.inorder[self.cur]

    def hasPrev(self) -> bool:
        return self.cur > 1
        

    def prev(self) -> int:
        self.cur-=1
        return self.inorder[self.cur]
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()