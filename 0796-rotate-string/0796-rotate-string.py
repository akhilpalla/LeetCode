# Same as STRSTR logic in leetcode 28
# if the string is rotated, it will be substring of original+orginal 
# T = N^2 S = 1
class Solution:
    def rotateString(self,text,pattern):
        if len(text) != len(pattern):
            return False

        text = text+text
        if pattern == "":
            return True

        for i in range(len(text) + 1 - len(pattern)):
            for j in range(len(pattern)):
                if text[i+j] != pattern[j]:
                    break
                if j == len(pattern) - 1:
                    return True
        return False


# KMP SOlution
# T = m+n S = m
class Solution:

    def computeLps(self, lps, pattern_length, pattern):
        length = 0
        i = 1
        while i < pattern_length:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    #we will check if can we have length-1 LPS
                    length = lps[length - 1]
                else:
                    # ex: pattern = [C D]
                    # LPS = [0]; now at D we now that length is 0 that means there is no prefix till now so LPS will be 0
                    lps[i] = 0
                    i += 1

    def kmpSearch(self, pattern, text):
        text_length = len(text)
        pattern_length = len(pattern)
        lps = [0] * pattern_length  # Longest prefix suffix array
        self.computeLps(lps, pattern_length, pattern)
        
        i = 0  # Index for text
        j = 0  # Index for pattern

        while (text_length - i) >= (pattern_length - j):
            if pattern[j] == text[i]:
                j += 1
                i += 1
            
            if j == pattern_length:
                return i - j  # Match found
            
            elif i < text_length and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1  # Match not found
    
    
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return self.kmpSearch(goal , s+s) != -1
        