class Solution:
    def maxDiff(self, num: int) -> int:
        a = b = 0
        n = len(str(num))
        nums = str(num)
        if nums[0]!= "1" and nums[0]!= "9":
            a = int(nums.replace(nums[0],"9"))
            b = int(nums.replace(nums[0],"1"))
            return a-b
        elif nums[0]=="1": 
            a = int(nums.replace("1","9"))
            b = num
            for i in range(0,n-1):
                if nums[i]!="1" and nums[i]!="0":
                    b = int(nums.replace(nums[i],"0"))
                    break 
            return a-b
        else: 
            a = num
            b = int(nums.replace("9","1"))
            for i in range(0,n-1):
                if nums[i]!=nums[i+1]:
                    a = int(nums.replace(nums[i+1],"9"))
                    break
            return a-b