# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        root.val = 0
        self.jvrc = []

        self.f(root)

    def f(self, root):
        q = deque([root])

        while q:
            l = len(q)

            for i in range(l):
                n = q.popleft()

                self.jvrc.append(n.val)

                if n.left is not None:
                    q.append(n.left)
                    n.left.val = (n.val*2)+1
                    
                if n.right is not None:
                    q.append(n.right)
                    n.right.val = (n.val*2)+2  


    def find(self, target: int) -> bool:

        if target in self.jvrc:
            return True

        return False                

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)