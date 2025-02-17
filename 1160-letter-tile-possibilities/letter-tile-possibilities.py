class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seq = set()
        cntr = collections.defaultdict(int)
        for char in tiles:
            cntr[char] += 1
        
        curr = list(cntr.keys())
        seq.update(curr)
        
        def calc_rem(char, d):
            dc = d.copy()
            dc[char] -= 1
            if dc[char] == 0:
                del dc[char]
            return dc
        
        for i, val in enumerate(curr):
            curr[i] = [val, calc_rem(val, cntr)]

        wl = 2
        while wl <= len(tiles):
            wl += 1
            ne_it = []
            for val, rem in curr:
                for char in rem:
                    ne =  val+char
                    if ne not in seq:
                        ne_it.append([ne, calc_rem(char, rem)])
                    seq.add(ne)
                    ne =  char+val
                    if ne not in seq:
                        ne_it.append([ne, calc_rem(char, rem)])
                    seq.add(ne)
            curr = ne_it
        return len(seq)