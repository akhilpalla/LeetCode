class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:

        def getNextMin(i, isLeft):
            dx = -1 if isLeft else 1
                 
            curr = i
            nxt = curr+dx
            while nxt >= 0 and nxt < len(heights) and heights[nxt] <= heights[curr]:
                curr = nxt
                nxt += dx
    
            if heights[curr] == heights[i]:
                return -1

            dx = -dx
            nxt = curr + dx
            while nxt >= 0 and nxt < len(heights) and heights[curr] == heights[nxt]:
                curr = nxt
                nxt += dx

            return curr

        for _ in range(volume):
            pos = getNextMin(k, True)
            if pos != -1:
                heights[pos] += 1
            else:
                pos = getNextMin(k, False)
                if pos != -1:
                    heights[pos] += 1
                else:
                    heights[k] += 1

        return heights

        