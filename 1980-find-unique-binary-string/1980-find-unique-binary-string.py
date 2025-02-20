class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""

        index = 0
        for bin_num in nums:
            ans = ans + str(1 - int(bin_num[index]))
            index+=1
        return ans