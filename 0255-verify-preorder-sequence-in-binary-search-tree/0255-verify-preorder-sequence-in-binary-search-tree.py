class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if not preorder: return True
        stk = [preorder[0]]
        floor = 0
        for val in preorder[1:]:
            if val < floor: return False
            while stk and stk[-1] < val:
                floor = stk.pop()
            stk.append(val)
        return True