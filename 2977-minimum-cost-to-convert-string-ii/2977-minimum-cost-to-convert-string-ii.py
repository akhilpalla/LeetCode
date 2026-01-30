class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        edges = defaultdict(lambda: defaultdict(lambda: inf))
        nodes = set()
        change_lens = set()
        
        for orig, change, c in zip(original, changed, cost):
            if edges[orig][change] > c:
                edges[orig][change] = c
            nodes.add(orig)
            nodes.add(change)
            change_lens.add(len(change))
        edges = {key: dict(value) for key, value in edges.items()}
        id2node = [None]*len(nodes)
        node2id = {}
        for i, node in enumerate(nodes):
            node2id[node] = i
            id2node[i] = node
        min_cost = [[inf]*len(nodes) for _ in range(len(nodes))]
        for node, i in node2id.items():
            min_cost[i][i] = 0
            if node not in edges:
                continue
            heap = [(c, node2id[b]) for b, c in edges[node].items() if c < inf]
            heapq.heapify(heap)
            while heap:
                c, j = heapq.heappop(heap)
                if min_cost[i][j] > c:
                    min_cost[i][j] = c
                    b = id2node[j]
                    if b in edges:
                        for b0, c0 in edges[b].items():
                            j0 = node2id[b0]
                            if c0 < inf and  c0+c < min_cost[i][j0]:
                                heapq.heappush(heap, (c0+c, j0))
        memo = {}
        def f(i):
            if i > len(source):
                return inf
            if i==len(source):
                return 0
            if i not in memo:
                value = inf
                for x in change_lens:
                    if i+x > len(source):
                        continue
                    s = source[i:i+x] 
                    if s in node2id:
                        k0 = node2id[s]
                        for k1, c in enumerate(min_cost[k0]):
                            if c < inf and target.startswith(id2node[k1], i):
                                val = c+f(i+x)
                                if val < value:
                                    value = val
                if source[i]==target[i]:
                    val = f(i+1)
                    if val < value:
                        value = val
                memo[i] = value 
            return memo[i]
        val = f(0)
        return val if val < inf else -1