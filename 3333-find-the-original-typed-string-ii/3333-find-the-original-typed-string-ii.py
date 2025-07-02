class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        bunks = []
        currl = ''
        curr = 0
        for i,a in enumerate(word):
            if a == currl:
                curr += 1
            else:
                bunks.append(curr)
                currl = a
                curr = 1
        bunks = bunks[1:]+[curr]
        n = len(word)
        mtotake = max(k-len(bunks),0)
        bunks = [b for b in bunks if b > 1]
        postbunk = [1]
        for bunk in bunks[::-1]:
            postbunk.append(postbunk[-1]*bunk%(10**9+7))

        postbunk = postbunk[::-1]
        m = len(bunks)

        if mtotake == 0:
            return postbunk[0]
        
        dp = [0]*(mtotake+1)
        dp[0] = 1
        prevsum = [0]
        for p in dp:
            prevsum.append((prevsum[-1]+p) % (10**9+7))

        for i in range(m-1,-1,-1):
            dp[0] = postbunk[i]
            newprevsum = [0,dp[0]]
            for j in range(1,mtotake+1):
                dp[j] = (prevsum[j+1] - prevsum[max(j-bunks[i]+1,0)]) % (10**9+7) 
                if j <= bunks[i]-1:
                    dp[j] += ((bunks[i]-1) - j) * postbunk[i+1] % (10**9+7)
                newprevsum.append((newprevsum[-1]+dp[j])% (10**9+7))
            prevsum = newprevsum

        return dp[-1] % (10**9+7)