class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        totalSum = 0
        valToCount = collections.defaultdict(int)
        for idx in range(M):
            for jdx in range(N):
                val = grid[idx][jdx]
                totalSum += val
                valToCount[val] += 1
        
        topSum = 0
        bottomSum = totalSum
        topElements = collections.defaultdict(int)
        botElements = valToCount.copy()
        for idx in range(M-1):
            curRow = 0
            for jdx in range(N):
                val = grid[idx][jdx]
                curRow += val
                topElements[val] += 1
                botElements[val] -= 1
                if botElements[val] == 0:
                    del botElements[val]
        
            topSum += curRow
            bottomSum -= curRow
            if topSum == bottomSum:
                return True
            elif topSum > bottomSum:
                diff = topSum - bottomSum
                if diff in topElements:
                    if idx == 0:
                        if diff != grid[0][0] and diff != grid[0][N-1]:
                            continue
                    
                    if N == 1:
                        if diff != grid[0][0] and diff != grid[idx][0]:
                            continue

                    return True
            else:
                diff = bottomSum - topSum
                if diff in botElements:
                    if idx == M-2:
                        if diff != grid[M-1][0] and diff != grid[M-1][N-1]:
                            continue

                    if N == 1:
                        if diff != grid[idx+1][0] and diff != grid[M-1][0]:
                            continue

                    return True
            

        leftSum = 0
        rightSum = totalSum
        leftElements = collections.defaultdict(int)
        rightElements = valToCount.copy()
        for jdx in range(N-1):
            curCol = 0
            for idx in range(M):
                val = grid[idx][jdx]
                curCol += val
                leftElements[val] += 1
                rightElements[val] -= 1
                if rightElements[val] == 0:
                    del rightElements[val]
                
            leftSum += curCol
            rightSum -= curCol
            if leftSum == rightSum:
                return True
            elif leftSum > rightSum:
                diff = leftSum - rightSum
                if diff in leftElements:
                    if jdx == 0:
                        if diff != grid[0][0] and diff != grid[M-1][0]:
                            continue

                    if M == 1:
                        if diff != grid[0][0] and diff != grid[0][jdx]:
                            continue

                    return True
            else:
                diff = rightSum - leftSum
                if diff in rightElements:
                    if jdx == N-2:
                        if diff != grid[0][N-1] and diff != grid[M-1][N-1]:
                            continue
                    
                    if M == 1:
                        if diff != grid[0][jdx+1] and diff != grid[0][N-1]:
                            continue

                    return True

        return False