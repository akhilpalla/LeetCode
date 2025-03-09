class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = defaultdict(int)
        count = 0

        for word in words:
            if seen[word[::-1]] > 0:
                count += 4 
                seen[word[::-1]] -= 1
            else:
                seen[word] += 1

        for word, val in seen.items():
            if word[0] == word[1] and val == 1:
                count += 2
                break 
        
        return count 