class Node:
    def __init__(self, v):
        self.val = v
        self.children = []

def addNumToTree(root, n):
    if not root:
        return
    q = deque([root])
    while q:
        t = q.popleft()
        if not t.children:
            t.children.append(Node(n))
            continue
        for i in range(len(t.children)):
            if n % t.children[i].val == 0:
                q.append(t.children[i])
                added = True
        if not q:
            t.children.append(Node(n))

def findDeepestSequence(root):
    cur, ans = [1], [1]
    def helper(node):
        nonlocal ans
        if not node.children:
            if len(cur) > len(ans):
                ans = cur.copy()
            return

        for i in range(len(node.children)):
            cur.append(node.children[i].val)
            helper(node.children[i])
            cur.pop()

    helper(root)
    return ans
        
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        # We add root with val == 1 independently if nums[0] == 1
        root = Node(1)
        for n in nums:
            if n != 1:
                addNumToTree(root, n)
        
        ans = findDeepestSequence(root)
        return ans if nums[0] == 1 else ans[1::]