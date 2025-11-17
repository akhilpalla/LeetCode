class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        currIdx = -1

        for i in range(n):
            if nums[i] == 1 and currIdx == -1:
                currIdx = i
            elif nums[i] == 1:
                # The expression abs(currIdx - i + 1) is equivalent
                # to (i - currIdx - 1), which is the count of
                # zeros between the two 1s.
                if abs(currIdx - i + 1) < k:
                    return False
                currIdx = i
        return True