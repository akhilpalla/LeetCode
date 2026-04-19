class Solution:
    def canForm(self, base_length, str1, str2, len_str1, len_str2):
        if len_str1 % base_length or len_str2 % base_length: 
            return False

        repetitions_str1 = len_str1 // base_length
        repetitions_str2 = len_str2 // base_length

        
        return str1 == repetitions_str1 * str1[:base_length] and \
         str2 == repetitions_str2 * str1[:base_length] 

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length_str1, length_str2 = len(str1), len(str2)

        for i in range(min(length_str1, length_str2), 0, -1):
            if self.canForm(i, str1, str2, length_str1, length_str2):
                return str1[:i]

        return ""

# T = min(m,n)*(mn)
# S = min(m,n)



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]

# T = S = M+N