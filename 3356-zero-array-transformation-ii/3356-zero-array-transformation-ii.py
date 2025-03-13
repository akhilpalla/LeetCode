class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        start = [0] * len(nums)
        end = [0] * len(nums)
        query_index = 0
        decrement_max = 0
        
        for index, num in enumerate(nums):
            decrement_max += start[index]
            while query_index < len(queries) and decrement_max < num:
                q_start, q_end, decrement = queries[query_index]
                start[q_start] += decrement
                end[q_end] += decrement
                if q_start <= index and q_end >= index:
                    decrement_max += decrement
                query_index += 1
            if decrement_max < num:
                return -1
            decrement_max -= end[index]
        return query_index