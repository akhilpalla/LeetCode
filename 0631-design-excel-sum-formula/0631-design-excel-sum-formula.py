class Excel:

    def __init__(self, height: int, width: str):
        self.g = {}
        self.cache = {}

    def set(self, row: int, column: str, val: int) -> None:
        key = column + str(row)
        self.g[key] = ("int", val)
        self.cache = {}

    def get(self, row: int, column: str) -> int:
        key = column + str(row)
        if key in self.cache:
            return self.cache[key]

        t, val = self.g.get(key, ("int", 0))
        ans = 0
        if t == "int":
            ans = val
        else:
            total = 0
            for v in val:
                col, row = v[0], int(v[1:])
                total += self.get(row, col)
            ans = total
        self.cache[key] = ans
        return ans

    def get_cells(self, range):
        beg, end = range.split(":")
        cells = []
        beg_col, beg_row = beg[0], int(beg[1:])
        end_col, end_row = end[0], int(end[1:])

        if beg_row > end_row:
            beg_row, end_row = end_row, beg_row

        if ord(beg_col) > ord(end_col):
            beg_col, end_col = end_col, beg_col

        curr_col, curr_row = ord(beg_col), beg_row
        while curr_col <= ord(end_col):
            while curr_row <= end_row:
                key = chr(curr_col) + str(curr_row)
                cells.append(key)
                curr_row += 1
            curr_row = beg_row
            curr_col += 1

        return cells

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        adj = []
        for num in numbers:
            if ":" in num:
                cells = self.get_cells(num)
                adj.extend(cells)
            else:
                adj.append(num)

        total = 0
        for a in adj:
            c, r = a[0], int(a[1:])
            v = self.get(r, c)
            if v != 0:
                print(f"{r=} {c=} {v=}")
            total += v

        key = column + str(row)
        print(f"sum setting {key=} to list {adj=} {total=}")
        self.g[key] = ("list", adj)
        self.cache = {}
        return total
# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)