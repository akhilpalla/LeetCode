class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        c = []
        
        for i, (p, h, d) in sorted(enumerate(zip(positions, healths, directions)), key=lambda x: x[1][0]):
            if len(c):
                while len(c):
                    if c[-1][1] == d:
                        c.append((h, d, i))
                        h = -1
                        break
                    elif c[-1][1] > d: # 'R' > 'L'
                        hh, dd, ind = c.pop()
                        if hh == h:
                            h = -1
                            break
                        elif hh < h:
                            h -= 1
                        else:
                            c.append((hh-1, dd, ind))
                            h = -1
                            break
                    else:
                        break
                if h > 0:
                    c.append((h, d, i))
            else:
                c.append((h, d, i))
        
        return [dd for dd, ddd, ind in sorted(c, key=lambda x: x[2])]
                            