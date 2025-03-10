# Brute: try all ways
def canReachEnd(jumps):
    def tryJump(currentIndex):
        # Base case: if we reach the last index, return True
        if currentIndex == len(jumps) - 1:
            return True
        
        # Determine the farthest we can jump from the current index
        maxReach = min(currentIndex + jumps[currentIndex], len(jumps) - 1)
        
        # Try all possible positions we can jump to
        for nextIndex in range(currentIndex + 1, maxReach + 1):
            if tryJump(nextIndex):
                return True
        
        # If no jump reaches the end, return False
        return False
    
    return tryJump(0)
# T = 2^n ==>where n is the length of array ||| S = N for recurssion  


#If array is having all positive numbers then we can for sure go the last element, we will have problem only if there are zeros in the array, because we should be able to cross the 0, if we cannot cross 0 and if we end up at zero then we cannot move from that place
#So while iterating the array keep track of maximum index we can go, and if at any index if maxIndex we can go is less than the current index that means we cannot cross that index bcoz of 0 return false 

class Solution:
                            
    def canJump(self,nums):
        max_index = 0

        for i in range(len(nums)):
            if i > max_index:
                return False

            max_index = max(max_index, i + nums[i])

        return True

#  T = N
#  S = 1    



