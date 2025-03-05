class Solution:
    def maxHeight(self, cuboids):
        n = len(cuboids)

        cuboids = [sorted(i) for i in cuboids]

        cuboids.sort(reverse = True)

        @lru_cache(None)
        def dfs(i,pl,pb,ph):
            if i >= n:
                return 0

            max_val = dfs(i+1,pl,pb,ph)

            if pl >= cuboids[i][0] and pb >= cuboids[i][1] and ph >= cuboids[i][2]:
                max_val = max(max_val,cuboids[i][2] + dfs(i+1,cuboids[i][0],cuboids[i][1],cuboids[i][2]))

            return max_val

        return dfs(0,float("inf"),float("inf"),float("inf"))