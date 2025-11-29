class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0 for _ in range(length)]
        diff = [0 for _ in range(length)]
        for list in updates:
            if list[0] < length:
                diff[list[0]] += list[2]
                if list[1] + 1 < length:
                    diff[list[1] + 1] -= list[2]
        ans[0] = diff[0]
        for i in range(1, length):
            ans[i] = ans[i - 1] + diff[i]
        return ans