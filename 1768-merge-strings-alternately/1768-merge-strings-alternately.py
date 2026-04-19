class Solution(object):
    def mergeAlternately(self, str1, str2):
        merged_string = []
        max_len = max(len(str1), len(str2))

        for idx in range(max_len):
            if idx < len(str1):
                merged_string.append(str1[idx])
            if idx < len(str2):
                merged_string.append(str2[idx])

        return ''.join(merged_string)

# T = M+N
# S = N for ans else 1