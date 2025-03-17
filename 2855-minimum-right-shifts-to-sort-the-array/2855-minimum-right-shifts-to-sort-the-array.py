class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        min_element = min(nums)
        shift_index = nums.index(min_element)
        
        # Generate the rotated list
        rotated_list = nums[shift_index:] + nums[:shift_index]
        
        # Check if it's sorted
        if rotated_list == sorted(nums):
            return (n - shift_index) % n
        
        return -1