class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        size = 1
        while size < n:
            size *= 2
        seg = [-1] * (2 * size)
        for i in range(n):
            seg[size + i] = baskets[i]
        for i in range(n, size):
            seg[size + i] = -1
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])
        def query(threshold):
            if seg[1] < threshold:
                return -1
            idx = 1
            while idx < size:
                if seg[2 * idx] >= threshold:
                    idx = 2 * idx
                else:
                    idx = 2 * idx + 1
            return idx - size
        def update(pos):
            pos += size
            seg[pos] = -1
            pos //= 2
            while pos:
                seg[pos] = max(seg[2 * pos], seg[2 * pos + 1])
                pos //= 2
        unplaced = 0
        for fruit in fruits:
            j = query(fruit)
            if j == -1:
                unplaced += 1
            else:
                update(j)
        return unplaced