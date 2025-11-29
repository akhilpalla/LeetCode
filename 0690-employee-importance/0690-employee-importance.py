"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        D = {i.id : e for e, i in enumerate(employees)}
        def dfs(id):
            ans = employees[D[id]].importance
            for i in employees[D[id]].subordinates:
                ans += dfs(i)
            return ans
        return dfs(id)