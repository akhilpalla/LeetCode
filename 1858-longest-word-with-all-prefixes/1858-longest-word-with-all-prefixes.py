class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.head = TrieNode()
    
    def addNode(self, word):
        tmp = self.head
        for w in word:
            if w not in tmp.children:
                tmp.children[w] = TrieNode()
            tmp = tmp.children[w]
        tmp.end = True
    
    def customSearch(self, node):
        # tmp = self.head
        cnt = ""
        t = ""
        for i in sorted(node.children):
            if node.children[i].end:
                m = i + self.customSearch(node.children[i])
                if len(cnt) < len(m):
                    cnt = m
        return cnt

class Solution:
    def longestWord(self, words: List[str]) -> str:

        inst = Trie()
        for i in words:
            inst.addNode(i)
        
        
        
        return inst.customSearch(inst.head)


        