class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = list(set(arr))
        temp.sort()
        
        dct = {}
        for i in range(len(temp)):
            dct[temp[i]] = i + 1

        ans = []
        for num in arr:
            ans.append(dct[num])
        
        return ans