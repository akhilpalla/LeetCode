class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start<end:
            s[start],s[end] = s[end], s[start]
            start+=1
            end-=1
        slicers = [i for i, val in enumerate(s) if val == " "]
        slicers.append(len(s))
        prev = 0
        for sliced in slicers:
            dummy = sliced - 1
            if s[prev] == " ":
                prev+=1
            while prev<dummy and prev<len(s)-1:
                s[prev], s[dummy] = s[dummy], s[prev]
                prev+=1
                dummy-=1
            prev=sliced+1