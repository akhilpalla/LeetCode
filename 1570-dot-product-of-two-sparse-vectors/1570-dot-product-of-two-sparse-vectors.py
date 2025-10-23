# CRACKING FAANG
#Brute: Linear Traversal

#BetterSOlution (Not Optimal, Optimal is below)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n              

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result
"""
Complexity Analysis
Let n be the length of the input array and L be the number of non-zero elements.

Time complexity: O(n) for creating the Hash Map; O(L) for calculating the dot product.

Space complexity: O(L) for creating the Hash Map, as we only store elements that are non-zero. O(1) for calculating the dot product.

"""

# #Optimal Solution
class SparseVector:
    def __init__(self, values: List[int]):
        self.non_zero_vals = []
        # Store only non-zero values and their indices.
        for idx, value in enumerate(values):
            if value != 0:
                self.non_zero_vals.append((idx, value))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, other_vec: 'SparseVector') -> int:
        result = 0
        ptr1 = ptr2 = 0
        # Traverse both vectors to compute the dot product.
        while ptr1 < len(self.non_zero_vals) and ptr2 < len(other_vec.non_zero_vals):
            idx1, val1 = self.non_zero_vals[ptr1]
            idx2, val2 = other_vec.non_zero_vals[ptr2]

            if idx1 == idx2:
                result += val1 * val2
                ptr1 += 1
                ptr2 += 1
            elif idx1 > idx2:
                ptr2 += 1
            else:
                ptr1 += 1

        return result



"""
for INIT
T = O(N)
S = O(N)

for DotProd
T = O(M+N)
S = O(M+N) (no extra it is just input)

"""
"""        
Follow up: What if only one of the vectors is sparse?
USE BINARY SEARCH
"""

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)