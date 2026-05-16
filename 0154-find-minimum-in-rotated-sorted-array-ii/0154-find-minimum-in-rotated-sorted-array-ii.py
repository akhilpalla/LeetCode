class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_num = float("inf")
        q = deque()
        q.append((l,r))

        while q:
            l,r = q.popleft()
            while l <= r: 
                mid = (l + r)//2 
                if nums[l] == nums[mid] == nums[r]: # If left and right and mid are all duplicates then we dont know which side to go hence we explore both sides
                    min_num = min(nums[l],min_num)
                    q.append((mid+1,r))
                    q.append((l,mid-1))
                    break
                if nums[l] <= nums[mid] <= nums[r]: # no rotated array
                    min_num = min(nums[l],min_num)
                    return min_num
                else:
                    if nums[l] <= nums[mid]: # left part is sorted, so we take the min of left and move towards right
                        min_num = min(nums[l],min_num)
                        l = mid+1
                    else: # right part is sorted, so we take the min of right and move towards left
                        min_num = min(nums[mid],min_num)
                        r = mid - 1
        return min_num