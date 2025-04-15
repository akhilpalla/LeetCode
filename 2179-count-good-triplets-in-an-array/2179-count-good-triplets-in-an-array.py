class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)

    def update(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        
        index_in_nums2 = {num: i for i, num in enumerate(nums2)}
        pos = [index_in_nums2[num] for num in nums1]

        left_tree = FenwickTree(n)
        right_tree = FenwickTree(n)

        for p in pos:
            right_tree.update(p, 1)

        res = 0
        for j in range(n):
            mid = pos[j]
            right_tree.update(mid, -1)

            left = left_tree.query(mid - 1)
            right = right_tree.query(n - 1) - right_tree.query(mid)

            res += left * right
            left_tree.update(mid, 1)

        return res