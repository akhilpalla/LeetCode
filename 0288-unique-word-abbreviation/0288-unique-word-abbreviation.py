class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.dictionary = dictionary
        self.d = defaultdict(set)
        for word in self.dictionary:
            if len(word)-2 < 1:
                w = word[0] + word[-1]
            else:
                w = word[0] + str(len(word)-2) + word[-1]
            if w not in self.d:
                self.d[w] = set()
                self.d[w].add(word)
            else:
                self.d[w].add(word)
    def isUnique(self, word: str) -> bool:
        if len(word)-2 < 1:
            w = word[0] + word[-1]
        else:
            w = word[0] + str(len(word)-2) + word[-1]
        return len(self.d[w]) == 0 or (len(self.d[w]) == 1 and word == list(self.d.get(w))[0])

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)