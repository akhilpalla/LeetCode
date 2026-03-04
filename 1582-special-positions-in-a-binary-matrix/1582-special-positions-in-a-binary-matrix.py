class Solution:
    def numSpecial(self, nums: List[List[int]]) -> int:
        result = 0
        columns = [0] * len(nums[0])

        for i in range(len(nums)):
            ones_in_the_row = 0
            column = 0

            for j in range(len(nums[i])):
                if nums[i][j] == 1:
                    ones_in_the_row += 1

                    if ones_in_the_row == 1:
                        columns[j] = 1 if columns[j] == 0 else 2
                        column = j
                    else:
                        columns[column] = 2
                        columns[j] = 2

        result += sum(column == 1 for column in columns)
        return result