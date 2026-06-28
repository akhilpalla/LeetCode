class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        nodes = deque([self.root])
        for char in word:
            found = False
            for _ in range(len(nodes)):
                node = nodes.popleft()
                if char == ".":
                    found = True
                    for child in node.children.values():
                        nodes.append(child)
                elif char in node.children:
                    found = True
                    nodes.append(node.children[char])
                else:
                    continue
            if not found:
                return False

        for node in nodes:
            if node.is_word:
                return True
        
        return False
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)