# Brute: Create a 3rd array and store the sorted elements in that and return median
# T = S = n1+n2
"""
def median(a, b):
    # size of two given arrays:
    n1, n2 = len(a), len(b)

    arr3 = []
    # apply the merge step:
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            arr3.append(a[i])
            i += 1
        else:
            arr3.append(b[j])
            j += 1

    # copy the left-out elements:
    arr3.extend(a[i:])
    arr3.extend(b[j:])

    # Find the median:
    n = n1 + n2
    if n % 2 == 1:
        return float(arr3[n // 2])

    median = (arr3[n // 2] + arr3[(n // 2) - 1]) / 2.0
    return median

"""

#====BETTER===============================
# Dont Store the elements in the array, just remmeber the location in pointers
"""
def median(a, b):
    n1, n2 = len(a), len(b)
    n = n1 + n2  # total size
    ind2 = n // 2
    ind1 = ind2 - 1
    cnt = 0
    ind1el, ind2el = -1, -1

    # apply the merge step:
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            if cnt == ind1:
                ind1el = a[i]
            if cnt == ind2:
                ind2el = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                ind1el = b[j]
            if cnt == ind2:
                ind2el = b[j]
            cnt += 1
            j += 1

    # copy the left-out elements:
    while i < n1:
        if cnt == ind1:
            ind1el = a[i]
        if cnt == ind2:
            ind2el = a[i]
        cnt += 1
        i += 1
    while j < n2:
        if cnt == ind1:
            ind1el = b[j]
        if cnt == ind2:
            ind2el = b[j]
        cnt += 1
        j += 1

    # Find the median:
    if n % 2 == 1:
        return float(ind2el)

    return float(ind1el + ind2el) / 2.0

T = n1+n2
S = 1
"""
#=================================================================================
#Optimal
class Solution:
    def findMedianSortedArrays(self, lis1: List[int], lis2: List[int]) -> float:

        n1, n2 = len(lis1), len(lis2)
        # if n1 is bigger swap the arrays:
        if n1 > n2:
            return self.findMedianSortedArrays(lis2 , lis1)

        n = n1 + n2  # total length
        left = (n1 + n2 + 1) // 2  # length of left half
        # apply binary search:
        low, high = 0, n1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            # calculate l1, l2, r1, and r2;
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid1 < n1:
                r1 = lis1[mid1]
            if mid2 < n2:
                r2 = lis2[mid2]
            if mid1 - 1 >= 0:
                l1 = lis1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = lis2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

            # eliminate the halves:
                        
            # total 10 elements ==> on left half we should have 5 elements

            # 1 3 4 7 | 10 12         l1>r2 ==> h = mid-1
            #       2 | 3 6 15

            # 1 3 4 | 7 10 12         correct
            #   2 3 | 6 15

            #   1 3 | 4 7 10 12       l2>r1 => l = mid+1
            # 2 3 6 | 15

            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0  # dummy statement
        
# Time Complexity: O(log(min(n1,n2)))
# S = 1