class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = text.split()
        for word in l[:]:  
            for j in brokenLetters:
                if j in word:
                    l.remove(word) 
                    break          
        return len(l)