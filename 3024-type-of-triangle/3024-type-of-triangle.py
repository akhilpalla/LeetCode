class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if(nums[0] + nums[1] > nums[2] 
            and nums[0] + nums[2] > nums[1]
            and nums[1] + nums[2] > nums[0]):
            
            ref = [nums[0] == nums[1], nums[1] == nums[2], nums[0] == nums[2]].count(True)
            if(ref == 1):
                return "isosceles"
            elif(ref == 3):
                return "equilateral"
            else:
                return "scalene"

        else:
            return "none"