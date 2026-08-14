class Solution:
    def getLength(self, nums):
        res = 0
        for i in range(len(nums)):
            subarray = {}
            freq = {}
            for j in range(i, len(nums)):
                if subarray.get(nums[j], 0) == 0:
                    subarray[nums[j]] = 1
                    freq[1] = freq.get(1, 0) + 1
                else:
                    curr = subarray[nums[j]]
                    freq[curr] -= 1
                    if freq[curr] == 0:
                        del freq[curr]
                    subarray[nums[j]] += 1
                    curr = subarray[nums[j]]
                    freq[curr] = freq.get(curr, 0) + 1
                if subarray[nums[j]] == (j - i + 1):
                    res = max(res, j - i + 1)
                elif len(freq) == 2:
                    small = min(freq)
                    large = max(freq)
                    if small * 2 == large:
                        res = max(res, j - i + 1)
        return res