class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left_product = [1] * n
        right_product = [1] * n
        result = [0] * n
        
        for i in range(1, n):
            left_product[i] = nums[i - 1] * left_product[i - 1]
        
        for j in range(n - 2, -1, -1):
            right_product[j] = nums[j + 1] * right_product[j + 1]
        
        for k in range(n):
            result[k] = left_product[k] * right_product[k]
        
        return result

# T = S = N

#Optimal
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        result = [1] * n
        
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        
        right_product = 1
        
        for j in range(n - 1, -1, -1):
            result[j] *= right_product
            right_product *= nums[j]
        
        return result

# T = N
# S = 1