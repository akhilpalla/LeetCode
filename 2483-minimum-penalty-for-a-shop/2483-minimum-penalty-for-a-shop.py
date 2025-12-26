class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefOpen = [0] * n
        sufClosed = [0] * n
 
        if customers[0] == 'N':
            prefOpen[0] = 1
        for i in range(1, n):
            prefOpen[i] = prefOpen[i - 1]
            if customers[i] == 'N':
                prefOpen[i] += 1
 
        if customers[n - 1] == 'Y':
            sufClosed[n - 1] = 1
        for i in range(n - 2, -1, -1):
            sufClosed[i] = sufClosed[i + 1]
            if customers[i] == 'Y':
                sufClosed[i] += 1
 
        ans = 0
        penalty = sufClosed[0]
 
        for i in range(1, n):
            if prefOpen[i - 1] + sufClosed[i] < penalty:
                penalty = prefOpen[i - 1] + sufClosed[i]
                ans = i
 
        if prefOpen[n - 1] < penalty:
            penalty = prefOpen[n - 1]
            ans = n
 
        return ans