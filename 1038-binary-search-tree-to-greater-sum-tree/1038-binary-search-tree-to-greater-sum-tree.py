class Solution:
    def bstToGst(self, root):
        self.total = 0
        def dfs(n):
            if n:
                dfs(n.right)
                self.total +=  n.val
                n.val       =  self.total
                dfs(n.left)
        dfs(root)
        return root