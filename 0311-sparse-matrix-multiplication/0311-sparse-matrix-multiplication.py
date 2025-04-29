class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def getSparseList(nums):
            sparse = []
            for i, n in enumerate(nums):
                if n:
                    sparse.append((n, i))

            return sparse

        
        def getSparseCols(k, n, mat, cols):
            for r in range(k):
                for c in range(n):
                    if mat[r][c]:
                        cols[c].append((mat[r][c], r))

                        
        def multiply(vec1, vec2):
            result = 0
            i1 = i2 = 0
            while i1 < len(vec1) and i2 < len(vec2):
                if vec1[i1][1] == vec2[i2][1]:
                    result += vec1[i1][0] * vec2[i2][0]
                    i1 += 1
                    i2 += 1
                elif vec1[i1][1] < vec2[i2][1]:
                    i1 += 1
                else:
                    i2 += 1
                    
            return result                    
                    
                        
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        
        rows1 = [getSparseList(row) for row in mat1]
        cols2 = [[] for _ in range(k)]
        getSparseCols(k, n, mat2, cols2)

        result = [[0] * n for _ in range(m)]
        for r in range(m):
            if rows1[r]:
                for c in range(n):
                    if cols2[c]:
                        result[r][c] = multiply(rows1[r], cols2[c])
        
        return result