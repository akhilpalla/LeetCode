class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vow = False
        con = False
        count = 0
        
        for w in word:
            if w.isalpha():
                count += 1
                if w.lower() in vowels:
                    vow = True
                else:
                    con = True
            elif w.isdigit():
                count += 1
            else:
                return False  # Invalid character
        
        return count >= 3 and vow and con