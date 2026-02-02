class HitCounter:

    def __init__(self):
        self.counter = []

    def hit(self, timestamp: int) -> None:
        self.counter.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return len(self.counter) - bisect_right(self.counter, timestamp - 300)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)