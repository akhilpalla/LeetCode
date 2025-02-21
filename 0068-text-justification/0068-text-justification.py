from typing import List

class Solution:
    def convertListToString(self, is_last: bool, L: List[str], maxWidth: int) -> str:
        if len(L) == 1:
            return L[0] + " " * (maxWidth - len(L[0]))
        
        if is_last:
            return " ".join(L) + " " * (maxWidth - len(" ".join(L)))
        
        total_chars = sum(len(word) for word in L)
        spaces = maxWidth - total_chars
        gaps = len(L) - 1
        
        if gaps == 0:
            return L[0] + " " * spaces
        
        space_per_gap = spaces // gaps
        extra_spaces = spaces % gaps
        
        result = []
        for i, word in enumerate(L[:-1]):
            result.append(word)
            result.append(" " * (space_per_gap + (1 if i < extra_spaces else 0)))
        
        result.append(L[-1])
        return "".join(result)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        results = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + len(current_line) <= maxWidth:
                current_line.append(word)
                current_length += len(word)
            else:
                results.append(self.convertListToString(False, current_line, maxWidth))
                current_line = [word]
                current_length = len(word)

        if current_line:
            results.append(self.convertListToString(True, current_line, maxWidth))

        return results