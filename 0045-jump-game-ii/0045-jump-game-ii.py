# Brute: try all possible ways and return minimum 
"""
def fun(arr,ind,jumps):
    if(ind>=n-1):
        return jumps #End reached
    
    mini = sys.maxsize
    for i in range(1,arr[ind]): #starting from 1 bcoz we dont want to jump to the same index
        mini = min(mini , fun(ind+i,jump+1))
    return mini

print("ans ",fun(arr,0,0))

T    = N^N
ASC  = N
"""
#=======================================================================================
"""
Better: Use DP

def fun(arr,ind,jumps):
    if(ind>=n-1):
        return jumps #End reached

    if dp[ind][jumps]!=-1:
        return dp[ind][jumps]    
    
    mini = sys.maxsize
    for i in range(1,arr[ind]): #starting from 1 bcoz we dont want to jump to the same index
        mini = min(mini , fun(ind+i,jump+1))
    dp[ind][jumps] =  mini
    return mini

print("ans ",fun(arr,0,0))

T    = N^2
ASC  = N^2
"""
#=======================================================================================
"""
Optimal: Use Ranges ie for example if arr is
arr = [2,3,1,4,1,1,1,2]
when we are at ind-0 we can jump to a max of ind-1 or ind-2 it will take 1 jump
        [2 , 3 , 1 , 4 , 1 , 1 , 1 , 2]
              ---
              1 jump 

        [2 , 3 , 1 , 4 , 1 , 1 , 1 , 2]
              ---     ----
              1 jump   2 J.  ---> this is because after first jump the max we can reach is this range

        [2 , 3 , 1 , 4 , 1 , 1 , 1 , 2]
              ---     ----    --------
             1 jump   2 J.      3 J
        
        so in 3 jumps we reach end 

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        l = r = 0
        
        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1
        
        return jumps

# T = N
# S = 1