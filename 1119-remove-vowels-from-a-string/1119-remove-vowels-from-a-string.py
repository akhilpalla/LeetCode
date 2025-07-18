class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([e if e not in set(['a', 'e','i','o','u']) else '' for e in s])