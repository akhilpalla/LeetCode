class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self._v = [v1[::-1], v2[::-1]]
        self.turn = 0
        if not v1:
            self.turn = 1

    def next(self) -> int:
        if self.hasNext:
            popped = self._v[self.turn % 2].pop() 
            if self.hasNext(1):
                self.turn += 1
            return popped
        else:
            raise RuntimeError('It is empty.')

    def hasNext(self, adjust = 0) -> bool:
        return len(self._v[(self.turn + adjust) % 2]) > 0


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())