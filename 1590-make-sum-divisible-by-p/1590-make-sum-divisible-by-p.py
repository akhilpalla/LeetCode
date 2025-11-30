# Find the smallest subarray that has a sum modulo equal to sum(nums)%p

# Brute: find all the subarray with sum(nums)%p and update the min --> n^2

class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        # If the total sum is already divisible by p, return 0
        if remainder == 0:
            return 0

        prefix_sum = 0
        # Dictionary to store the prefix sums mod p and their indices
        mp = {0: -1}   # to handle the case where entire prefix needs to be removed ie when 
        # arr [................. 2 2 2 2]
        # ind  0.                5 6 7 8
        # we have to remove 0 to 5 to make rem divisble by 2
        # at this point we will have our target 0.
       
        min_len = 99999999999999999999

        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_sum %= p

            # We need to find the prefix that makes the current subarray divisible by p
            #we are again doing mod p because target can to negative and we only have positive so we are 
            #brining back into the range
            target = (prefix_sum - remainder) % p

            if target in mp:
                min_len = min(min_len, i - mp[target])

            mp[prefix_sum] = i

        #this is because the question gave we cannot remove full array
        return min_len if min_len < len(nums) else -1
