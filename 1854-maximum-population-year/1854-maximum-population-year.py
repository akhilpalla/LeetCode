class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        min_year, max_year = 2051, 1949
        for (start, end) in logs:
            if start < min_year:
                min_year = start
            if end > max_year:
                max_year = end
        years = [0]*(max_year-min_year+1)
        for (start, end) in logs:
            years[start-min_year] += 1
            years[end-min_year] -= 1
        alive, res, year = 0, 0, 0
        for i in range(min_year, max_year+1):
            alive += years[i-min_year]
            if alive > res:
                res = alive
                year = i
        return year