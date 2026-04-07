class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perim = max(1, 2 * (width + height) - 4)
        self.pos = 0

        self.east_end = self.w - 1
        self.north_end = self.east_end + self.h - 1
        self.west_end = self.north_end + self.w - 1

        self.moved = False

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % self.perim
        self.moved = True

    def getPos(self) -> List[int]:
        p = self.pos

        if p == 0:
            return [0, 0]

        if p <= self.east_end:
            return [p, 0]

        if p <= self.north_end:
            offset = p - self.east_end
            return [self.w - 1, offset]

        if p <= self.west_end:
            offset = p - self.north_end
            return [self.w - 1 - offset, self.h - 1]

        offset = p - self.west_end
        return [0, self.h - 1 - offset]

    def getDir(self) -> str:
        if self.pos == 0 and self.moved:
            return "South"

        if self.pos <= self.east_end:
            return "East"
        if self.pos <= self.north_end:
            return "North"
        if self.pos <= self.west_end:
            return "West"
        return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()