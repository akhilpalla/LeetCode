class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        return [list(x)[::-1] for x in zip(*[itertools.chain.from_iterable([sorted(g, reverse = True) for _, g in groupby(row, lambda x: x != '*')]) for row in box])]
 