class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        hash_table = {}
        def avg_sum (i,k):
            if k == 1:
                return sum(nums[i:]) /len(nums[i:])
            if (i,k) in hash_table:
                return hash_table[(i,k)]
            cur_sum = 0
            size =0
            res = float('-inf')
            cur_avg = 0
            for j in range(i,len(nums)-k+1):
                cur_sum += nums[j]
                size+=1
                cur_avg = cur_sum /size
                right_side_avg = avg_sum(j+1,k-1)
                total_avg = cur_avg + right_side_avg
                res = max(total_avg,res)
            hash_table[(i,k)] = res
            return res
        return avg_sum(0,k)