# Brute: Generate all the substrings 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                
                if substring == substring[::-1]:
                    if len(substring) > len(longest_palindrome):
                        longest_palindrome = substring
        
        return longest_palindrome

# T = N^3 S = 1

class Solution:
    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # When the loop breaks, `left` and `right` are one step beyond the palindrome bounds
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n < 2:
            return s

        leftBound, rightBound = 0, 0

        for i in range(n):
            # Check palindrome centered at i (odd length)
            oddLeftBound, oddRightBound = self.expand_around_center(s, i, i)
            # Check palindrome centered between i and i+1 (even length)
            evenLeftBound, evenRightBound = self.expand_around_center(s, i, i + 1)

            # Update the result with the longer palindrome for odd length
            if oddRightBound - oddLeftBound > rightBound - leftBound:
                leftBound, rightBound = oddLeftBound, oddRightBound
            # Update the result with the longer palindrome for even length
            if evenRightBound - evenLeftBound > rightBound - leftBound:
                leftBound, rightBound = evenLeftBound, evenRightBound

        return s[leftBound:rightBound + 1]

# T = n^2
# S = 1