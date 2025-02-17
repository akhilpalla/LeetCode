#Brute:
# for every element search other element in array n^2 solution 

#Better:
# sort the array and for every element do a BS to search the other array
#nlogn + nlogn

# Optimal Depending type of problem
# if only yes or no 
#sort and 2 pointer 
# nlogn + n
# space is 1

#if want indices then below is optimal
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            if target - nums[i] in h:
                return [h[target-nums[i]] , i]
            else:
                h[nums[i]] = i

# T = S = N