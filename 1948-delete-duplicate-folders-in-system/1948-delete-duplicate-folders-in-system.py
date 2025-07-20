class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.delete = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()
        patterns = defaultdict(list)
        ans = []

        self.populate_trie(root, paths)
        self.generate_patterns(root, patterns)
        self.update_node_status(patterns)
        self.generate_valid_paths(root, [], ans)
        
        return ans
        
    def populate_trie(self, root, paths):
        for path in sorted(paths):
            node = root
            for c in path:
                node = node.children[c]

    def generate_patterns(self, node, patterns):
        pattern = f'({"".join(child + self.generate_patterns(node.children[child], patterns) for child in node.children)})'

        if pattern != "()":
            patterns[pattern].append(node)

        return pattern

    def update_node_status(self, patterns):
        for pattern in patterns:
            if len(patterns[pattern]) > 1:
                for node in patterns[pattern]:
                    node.delete = True

    def generate_valid_paths(self, node, path, ans):
        if path:
            ans.append(path[:])
        
        for child in node.children:
            if not node.children[child].delete:
                self.generate_valid_paths(node.children[child], path + [child], ans)