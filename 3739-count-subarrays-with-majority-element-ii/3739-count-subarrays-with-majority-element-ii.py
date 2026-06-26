class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pos = []
        neg = []
        zero = 0
        pos_sum = 0
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                pos.append(zero)
                pos_sum += zero + 1
                if len(neg) >= 1:
                    zero = neg.pop()
                else:
                    zero = 0
                pos[-1] += 1
            else:
                neg.append(zero)
                neg[-1] += 1
                if len(pos) >= 1:
                    zero = pos.pop()
                    pos_sum -= zero
                else:
                    zero = 0
            ans += pos_sum
        return ans