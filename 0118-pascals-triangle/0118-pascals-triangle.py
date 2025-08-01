# Type-1: Print the element at R=5 C=3
# formula = (r-1) C (c-1)
# element at(5,3) is 4c2 ie (4*3)/(2*1)
"""
fun(r,c):
    res=1
    for i in range(c):
        res = res*(r-1)
        res = res/(i+1)
    return res
T = O(r) here r is from nCr
S = 1
"""
#==========================TYPE-2=========================

# Type2 Print Row: nth row will always have n elements
# by above method time will be more ie O(NR)

"""
Better: for 6th row 
1 5/1 (5*4)/(1*2) (5*4*3)/(1*2*3) .. .. .. ...
ie 
ans = 1
print(ans)
for i in range(1,n):
    ans = ans(n-i)
    ans = ans/i
    print(ans)
T = N
S = 1
"""

#==========================TYPE-3=========================
# print entire triangle
# use typ2 method n times done

class Solution:
    def generateRow(self,row):
        ans = 1
        ansRow = [1] #inserting the 1st element
        
        #calculate the rest of the elements:
        for col in range(1, row):
            ans *= (row - col)
            ans //= col
            ansRow.append(ans)
        return ansRow

    def generate(self, n: int) -> List[List[int]]:
        ans = []

        #store the entire pascal's triangle:
        for row in range(1, n+1):
            ans.append(self.generateRow(row))
        return ans
    
# T = S = n^2