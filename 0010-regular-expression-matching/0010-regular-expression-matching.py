class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DP table initialization
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Empty string matches with empty pattern
        
        # Deal with patterns like a*, a*b*, a*b*c*
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Match zero occurrences of character before '*'
                    dp[i][j] = dp[i][j - 2]
                    # Match one or more occurrences if the character before '*' matches
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[len(s)][len(p)]
# T = S = S*P
"""

dp[0][0] = True
dp[0][j] = dp[0][j - 2] if p[j - 1] == '*'  # Handles patterns like "a*", "a*b*"

dp[i][j] = dp[i - 1][j - 1] if p[j - 1] == '.' or p[j - 1] == s[i - 1]  # Match single character

dp[i][j] = dp[i][j - 2]  # Match zero occurrences with '*'
dp[i][j] = dp[i][j] or dp[i - 1][j] if p[j - 2] == '.' or p[j - 2] == s[i - 1]  # Match one or more occurrences with '*'

"""