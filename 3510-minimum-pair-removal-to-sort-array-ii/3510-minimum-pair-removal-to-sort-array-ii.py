from heapq import heappush, heappop, heapify
class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        nums.append(float("inf"))   
        left = [-1] + list(range(n))  
        right = list(range(1, n + 1))  
        heap = [(nums[i] + nums[i+1], i) for i in range(n - 1)]
        heapify(heap)
        bad = sum(nums[i] > nums[i + 1] for i in range(n - 1))
        ans = 0
        while bad > 0:
            total, i = heappop(heap)
            j = right[i]
            if left[j] != i or nums[i] + nums[j] != total:
                continue
            rr = right[j]
            pre_bad = int(nums[left[i]] > nums[i]) + int(nums[i] > nums[j]) + int(nums[j] > nums[rr])
            nums[i] = total
            right[i] = rr
            if rr < len(nums):
                left[rr] = i
            post_bad = int(nums[left[i]] > nums[i]) + int(nums[i] > nums[rr])
            bad += post_bad - pre_bad
            if left[i] >= 0:
                heappush(heap, (nums[left[i]] + nums[i], left[i]))
            if rr < n:
                heappush(heap, (nums[i] + nums[rr], i))
            ans += 1
        return ans