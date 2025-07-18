class Solution:
    def minimumDifference(self, nums):
        n = len(nums)//3

        left, right, mid = [-i for i in nums[:n]], nums[2*n:], nums[n:2*n]

        left_sum, right_sum = [-sum(left)], [sum(right)]

        heapq.heapify(left)
        heapq.heapify(right)

        for i in mid:
            heapq.heappush(left,-i)
            left_sum.append(left_sum[-1] + i + heapq.heappop(left))

        for i in mid[::-1]:
            heapq.heappush(right,i)
            right_sum.append(right_sum[-1] + i - heapq.heappop(right))

        right_sum = right_sum[::-1]

        return min([i-j for i,j in zip(left_sum,right_sum)])
