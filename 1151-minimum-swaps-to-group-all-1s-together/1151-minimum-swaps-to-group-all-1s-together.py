class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = data.count(1)
        min_swaps = zero_count = data[:ones].count(0)
        for i in range(1, len(data)-ones+1):
            if data[i-1] != data[i+ones-1]:
                zero_count += 1 if data[i+ones-1] == 0 else -1
            min_swaps = min(min_swaps, zero_count)
        return min_swaps