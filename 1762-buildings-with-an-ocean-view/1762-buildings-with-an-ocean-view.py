"""
Naive:
start traversing from left and for each element check if it is the greatest element comapred to everyone on the right, If it is greatest add it to the ans array
T = N^2

"""
#=====================================
"""
Optimal: travserse from right and keep track of max height soFar and check if current is greater than max height

T = N
S = N(for storing the answer)
"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = -1
        ans = []
        n = len(heights)
        for i in range(n-1,-1,-1):
            if heights[i] > maxHeight:
                ans.append(i)
                maxHeight = heights[i]

        return ans[::-1]

        