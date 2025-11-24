class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        str_arr = list()
        res = list()
        for i in nums:
            str_arr.append(str(i))
            res.append(int("".join(str_arr), 2) % 5 == 0)
                # res.append(True)
        return res