# Brute
class Solution:
    def minMoves(self, arr):
        smallest, largest = 0, len(arr) - 1
        moves = 0
        
        while True:
            # Find the indices of the minimum and maximum elements
            for idx in range(len(arr)):
                if arr[idx] > arr[largest]:
                    largest = idx
                if arr[idx] < arr[smallest]:
                    smallest = idx
            
            # Calculate the difference between the largest and smallest elements
            difference = arr[largest] - arr[smallest]
            
            # If the difference is zero, all elements are equal, so we stop
            if difference == 0:
                break
            
            # Increment the move count by the difference
            moves += difference
            
            # Increment all elements except the largest one by the difference
            for idx in range(len(arr)):
                if idx != largest:
                    arr[idx] += difference
        
        return moves

# T = n^2 
# S = 1

# Better
class Solution:
    def minMoves(self, arr):
        arr.sort()  # Sort the array
        total_moves = 0
        
        # Iterate from the last element down to the second element
        for idx in range(len(arr) - 1, 0, -1):
            total_moves += arr[idx] - arr[0]  # Subtract the smallest element from each
        
        return total_moves

# T = nlogn
# S = n for sorting

# Optimal
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        currMin=min(nums)
        ans=0
        for i in nums:
            ans+=i-currMin
        return ans

# T = n
# S = 1