class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hill_or_valley_set, N = set(), len(nums)
        def find_next_no_equal_on_right(i):
            key = nums[i]
            if i == N-1:
                return (None,None)
            for t in range(i+1,N):
                if nums[i] == nums[t]:
                    continue
                else:
                    if nums[i]<nums[t]:
                        return("up",t)
                    else:
                        return ("down",t)
            return (None,None)
        def find_next_no_equal_on_left(i):
            key = nums[i]
            if i == 0:
                return (None,None)
            for t in range(i,-1,-1):
                if nums[i] == nums[t]:
                    continue
                else:
                    if nums[i]<nums[t]:
                        return("up",t)
                    else:
                        return ("down",t)
            return (None,None)
        for i in range(1,len(nums)-1):
            L, R = find_next_no_equal_on_left(i),find_next_no_equal_on_right(i)
            if L[0] and R[0] and L[0] == R[0]:
                hill_or_valley_set.add((L[1],R[1]))
        return len(hill_or_valley_set)