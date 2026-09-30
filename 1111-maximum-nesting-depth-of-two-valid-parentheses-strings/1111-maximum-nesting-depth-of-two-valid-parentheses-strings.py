class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        seq = list(seq)
        st = []
        ans = [-1] * n 
        for  i,ele in enumerate(seq):
            if ele == '(':
                if st :
                    if st[-1] == 0:
                        st.append(1)
                        ans[i] = 1
                    elif st[-1] == 1:
                        st.append(0)
                        ans[i] = 0
                else:
                    st.append(1)
                    ans[i] = 1
            else:
                ans[i] = st.pop()
        return ans