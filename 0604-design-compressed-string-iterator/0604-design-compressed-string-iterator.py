class StringIterator:

    def __init__(self, compressedString: str):
        word = []
        cur = ""
        curnum = ""
        for c in compressedString:
            if c.isalpha():
                word.append(cur*(int(curnum) if curnum else 0))
                cur = c
                curnum = ""
            else:
                curnum += c 
        word.append(cur*int(curnum))
        self.i = 0 
        self.word = "".join(word)

    def next(self) -> str:
        if self.i < len(self.word):
            res = self.word[self.i]
            self.i += 1
            return res
        return " " 

    def hasNext(self) -> bool:
        return self.i < len(self.word)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()