class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0 
        right = None
        for i, item in enumerate(fruits):
            if item[0] >= startPos:
                if item[0] != startPos:
                    fruits.insert(i, (startPos, 0))
                right = i
                break
        if right is None:
            right = len(fruits)
            fruits.append((startPos, 0))
        indexofstart = right
        ans = 0
        cursum = 0
        for i in range(left, right):
            cursum += fruits[i][1]
        while right < len(fruits) and left <= indexofstart:
            while right < len(fruits) and 2 * min(startPos - fruits[left][0], fruits[right][0] - startPos) + max(startPos - fruits[left][0], fruits[right][0] - startPos) <= k:
                cursum += fruits[right][1]
                ans = max(ans, cursum)
                right += 1
            cursum -= fruits[left][1]
            left += 1
            

        return ans