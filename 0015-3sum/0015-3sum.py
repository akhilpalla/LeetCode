# Brute:
# Try out all the triplets
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if a[i]+a[j]+a[k] == 0:
#                 set.add([i,j,k].sort())
# sort is as good as constant 
# total time is n^3
# space is 2*(numberOfUniqueTriplets) (set and ans array)

####----Better---HASHING---############################################################
# in the above solution we are using 3 loops, to make it n^2 we have to eliminate one loop we do it by using hashing (3rd element = -(1st + 2nd))
# we store the elements in set we saw till now for quick loopups and use 2 loops, we should not store every element because we may have to check for index also, if we only store the elements we saw till now, we will be sure that the element in the set is not the same element from current if there are repeats as we moved from it 

"""
def triplet(n, arr):
    st = set()

    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            # Calculate the 3rd element:
            third = -(arr[i] + arr[j])

            # Find the element in the set:
            if third in hashset:
                temp = [arr[i], arr[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])

    # store the set in the answer:
    ans = list(st)
    return ans
T = n^2
S = O(2 * no. of the unique triplets) + O(N) as we are using a set data structure and a list to store the triplets and extra O(N) for storing the array elements in another set.
"""
####----Optimal---Space-Reduce---Sort---2Pointer-######################################################
# We were using the set to filter out duplicate triplets, we can avoid this by sorting 
# fix i pointer and use j and k to increase or decrease the sum accordingly if it is greater or less
# once the triplet is found skip all the elements which are same to avid the dups, this can be done easily bcoz if it is soirted array and all dups will be together

class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        n = len(arr)
        for i in range(n):
            # remove duplicates:
            if i != 0 and arr[i] == arr[i - 1]:
                continue

            # moving 2 pointers:
            j = i + 1
            k = n - 1
            while j < k:
                total_sum = arr[i] + arr[j] + arr[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    temp = [arr[i], arr[j], arr[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    # skip the duplicates:
                    while j < k and arr[j] == arr[j - 1]:
                        j += 1
                    while j < k and arr[k] == arr[k + 1]:
                        k -= 1

        return ans

# T = N^2
# S = 1