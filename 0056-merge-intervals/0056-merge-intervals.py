#Brute:
# iterate through every interval and check for overlap, if there is overlap merge those two and start from first again 


class Solution:
    def merge(self, intervals):
        i = 0
        while i < len(intervals):
            merged = False
            for j in range(i + 1, len(intervals)):
                # Check if intervals overlap
                if intervals[i][0] <= intervals[j][1] and intervals[j][0] <= intervals[i][1]:
                    # Merge intervals[i] and intervals[j]
                    new_interval = [
                        min(intervals[i][0], intervals[j][0]),
                        max(intervals[i][1], intervals[j][1])
                    ]
                    # Remove the original intervals and add the merged interval
                    intervals.pop(j)
                    intervals[i] = new_interval
                    merged = True
                    break  # Start over as merging may affect other intervals
            if not merged:
                i += 1
        return intervals
# T = N^2
# S = 1



#=======OPTIMAL-->we will do in single iteration---===============================
class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:


        n = len(arr) # size of the array

        # sort the given intervals:
        arr.sort()

        ans = []

        for i in range(n):
            # if the current interval does not
            # lie in the last interval:
            if not ans or arr[i][0] > ans[-1][1]:
                ans.append(arr[i])
            # if the current interval
            # lies in the last interval:
            else:
                ans[-1][1] = max(ans[-1][1], arr[i][1])
        return ans

# Time Complexity: O(N*logN) + O(N)
# Space Complexity: O(N)