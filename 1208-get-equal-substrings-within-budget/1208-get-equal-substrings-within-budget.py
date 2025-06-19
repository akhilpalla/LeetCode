class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        left = 0
        cost = 0
        maxLength = 0

        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))

            if cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            else: 
                length = right - left + 1
                if length > maxLength:
                    maxLength = length 


        return maxLength 



