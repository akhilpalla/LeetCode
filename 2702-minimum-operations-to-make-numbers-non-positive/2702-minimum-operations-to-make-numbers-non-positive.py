import numpy as np
class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        if max(nums) < 0 or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return ceil( float(nums[0]/x) )
        elif max(nums) == min(nums): 
            val = max(nums)
            if y > val:
                return 1
            else:
                k = val//( y*len(nums) + x-y )  
                residual = val%( y*len(nums) + x-y )  
                if residual > 0:
                    remainder = min(len(nums),ceil(residual/y))
                else:
                    remainder = 0
                return k*len(nums) + remainder
        else:
            def check_if_feasible( mid ):
                residual = [max(0, elem - mid*y) for elem in nums]
                x_ops = sum( [ceil(val/(x-y)) for val in residual] )
                return ceil(x_ops) <= mid
            lb = ceil(float(max(nums)/x))
            ub = ceil(float(max(nums)/y))
            while( abs(ub - lb) > 1 ):
                mid = ( ub + lb )//2
                check = check_if_feasible(mid)
                if check == True:  
                    ub = mid
                else:
                    lb = mid  
            return (lb if check_if_feasible(lb) == True else ub)               
          
        