class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences_by_prefix = collections.defaultdict(collections.defaultdict)
        self.input_chars = []
        self.frequency = collections.defaultdict(int)
        for sentence, time in zip(sentences, times):
            self.frequency[sentence] = time
            self.add_sentence(sentence, time)

    def add_sentence(self, sentence, time):
        for i, ch in enumerate(sentence):
            self.sentences_by_prefix[sentence[:i + 1]][sentence] = time

    def input(self, c: str) -> List[str]:
        result = []
        if c == '#':
            prefix = ''.join(self.input_chars)
            self.frequency[prefix] += 1
            self.add_sentence(prefix, self.frequency[prefix])
            self.input_chars = []
        else:
            self.input_chars.append(c)
            prefix = ''.join(self.input_chars)
            sorted_by_time_then_ascii = sorted(self.sentences_by_prefix[prefix].items(), key=lambda kv: (-kv[1], kv[0]))
            result = [sent for sent, score in sorted_by_time_then_ascii[:3]]
        return result
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)