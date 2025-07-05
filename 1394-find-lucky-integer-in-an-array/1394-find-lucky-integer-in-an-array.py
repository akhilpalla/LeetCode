class Solution:
    def findLucky(self, arr: List[int]) -> int:
        container = [0] * (max(arr) + 1)
        maximum = -1
        for i in arr:
            container[i] = container[i] + 1
        
        for i in range(1,len(container)):
            if container[i] == i:
                maximum = max(maximum, i)

        return maximum