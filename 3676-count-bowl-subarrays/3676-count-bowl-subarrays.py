class Solution:
    def ngr(self, l: List[int]) -> List[int]:
        n = len(l)
        st = []
        res = [-1] * n
        for i in range(n):
            while st and l[i] > l[st[-1]]:
                ind = st.pop()
                res[ind] = i
            st.append(i)
        return res
    
    def ngl(self, l: List[int]) -> List[int]:
        n = len(l)
        st = []
        res = [-1] * n
        for i in range(n):
            while st and l[i] > l[st[-1]]:
                st.pop()
            if st:
                res[i] = st[-1]
            st.append(i)
        return res

    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ng_r = self.ngr(nums)
        ng_l = self.ngl(nums)
        c = 0
        for i in range(n):
            if ng_r[i] != -1 and ng_l[i] != -1:
                c += 1
        return c