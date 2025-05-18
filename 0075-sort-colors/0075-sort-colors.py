#Brute: Sort the array nlogn
#Better: get counts of each and write back into the array extra space of O(3) and T is 2N
"""
def sortArray(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    for num in arr:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    for i in range(cnt0):
        arr[i] = 0

    for i in range(cnt0, cnt0 + cnt1):
        arr[i] = 1

    for i in range(cnt0 + cnt1, len(arr)):
        arr[i] = 2
"""

#=============================================================================
# Optimal: Dutch National Flag Algorithm 
"""
0 to low-1    ===> 0's
low to mid-1  ===> 1'2
mid to high   ===> unsorted
high+1 to n-1 ===> 2's

initial config
low = mid = 0
high = n-1
mid to high is still unsorted 

rules:
if a[mid] == 0:
    swap a[low] and a[mid]
    low++
    mid++
if a[mid] == 1:
    mid++
if a[mid] == 2:
    swap a[mid] and a[high]
    h--
"""
class Solution:
    def sortColors(self, arr: List[int]) -> None:
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

# T = N
# S = 1