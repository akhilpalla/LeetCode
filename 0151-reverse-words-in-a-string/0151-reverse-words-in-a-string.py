# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(reversed(s.split()))

        
class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove extra spaces and store words
        result = []
        word = []
        
        # Step 1: Extract words and handle spaces
        for char in s:
            if char != ' ':
                word.append(char)
            elif word:  # Found a space and have a word
                result.append(''.join(word))
                word = []
        
        # Add last word if exists
        if word:
            result.append(''.join(word))
            
        # Step 2: Reverse words list
        left, right = 0, len(result) - 1
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
            
        # Step 3: Join with spaces
        return ' '.join(result)

# T = 2N (for removing space and reversing)
# S = max length of word (for word array) result is for ans so not considered


#======Single Iteration Using Queue
class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove extra spaces and store words
        result = deque()
        word = []
        
        # Step 1: Extract words and handle spaces
        for char in s:
            if char != ' ':
                word.append(char)
            elif word:  # Found a space and have a word
                result.appendleft(''.join(word))
                word = []
        
        # Add last word if exists
        if word:
            result.appendleft(''.join(word))

        # Step 2: Join with spaces
        return ' '.join(result)

# T = N
# S = max length of word (for word array) result is for ans so not considered