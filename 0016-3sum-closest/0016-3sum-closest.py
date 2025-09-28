# Brute: Sort the array, and keeping one element fix check for the sum in remaining using 2 pointer
# T = nlogn + n^2
# S = n for sorting

"""
class Solution:
    def threeSumClosest(self, numbers: List[int], target_value: int) -> int:
        numbers.sort()
        min_diff = sys.maxsize

        for index in range(len(numbers)):
            left, right = index + 1, len(numbers) - 1
            while left < right:
                current_sum = numbers[index] + numbers[left] + numbers[right]
                if abs(target_value - current_sum) < abs(min_diff):
                    min_diff = target_value - current_sum
                if current_sum < target_value:
                    left += 1
                else:
                    right -= 1
            if min_diff == 0:
                # Found the exact target, no need to continue
                break
        #we are returning target-diff because we are minimising the diff, so target-diff will be close to the target
        return target_value - min_diff
"""

#==========OPTIMAL===================================
import bisect
# Using binary search
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # we will search for 3rd element in the array using BS
                complement = target - nums[i] - nums[j]
                #we will compute the upper bound of 3rd element 
                hi = bisect.bisect_right(nums, complement, j + 1) #both UB and LB will work here
                #we will also calcuate for one element less than UB because if compliment is 4 and UB is 15 diff is more
                # one element less than that can be 2 so diff is small here
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff

# T = N*NlogN
# S  = N for sorting