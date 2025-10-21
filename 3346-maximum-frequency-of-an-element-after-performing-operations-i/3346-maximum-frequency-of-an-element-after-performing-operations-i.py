class Solution:
    def maxFrequency(self, nums, k, numOperations):
        dict1, left, right, window_size, max_val = Counter(nums), 0, 0, 0, 1 
        nums.sort()
        for num in range(nums[0],nums[-1]+1):
            while nums[left] < num-k:
                left += 1 
                window_size -= 1 
            while right != len(nums) and nums[right] <= num+k:
                right += 1 
                window_size += 1 
            max_val = max(max_val,dict1[num]+min(numOperations,window_size-dict1[num]))
        return max_val 