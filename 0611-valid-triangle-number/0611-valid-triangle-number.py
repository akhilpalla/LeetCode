class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if(len(nums) < 3):
            return 0
        nums.sort()
        ans = 0
        k = len(nums) - 1
        while(k >= 0):
            i = 0
            j = k - 1
            while(i < j):
                if(nums[i] + nums[j] > nums[k]):
                    ans += (j - i)
                    j -= 1
                else:
                    i += 1
            k -= 1  
        return ans      