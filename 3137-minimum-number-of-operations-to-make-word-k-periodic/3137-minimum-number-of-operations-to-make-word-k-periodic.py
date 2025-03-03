class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        parts = []
        i = 0
        while i < len(word):
            parts.append(word[i:i+k])
            i += k
        
        cnt = Counter(parts)
        temp = temp_val = 0
        for k, v in cnt.items():
            if v > temp_val:
                temp = k
                temp_val = v
        
        return sum(cnt.values()) - temp_val