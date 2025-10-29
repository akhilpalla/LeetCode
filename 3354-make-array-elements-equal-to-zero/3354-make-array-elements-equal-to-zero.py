class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0 
        valid_count = 0 
        for i in range(n):
            right_sum = total_sum - left_sum 
            if nums[i] == 0:
                if right_sum == left_sum:
                    valid_count += 2 
                elif abs(right_sum - left_sum) == 1:
                    valid_count += 1 
            left_sum += nums[i]
        return valid_count