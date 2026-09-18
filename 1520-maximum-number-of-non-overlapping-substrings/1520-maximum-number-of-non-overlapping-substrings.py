class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        posLocation = defaultdict(list)
        for i, ch in enumerate(s):
            if len(posLocation[ch]) >= 2:
                posLocation[ch].pop()
            if not posLocation[ch]:
                posLocation[ch].append(i)
            posLocation[ch].append(i)
        setResult = set()
        for key, val in posLocation.items():
            st, ed = val[0], val[1]
            beg = st
            isValid = True
            while beg <= ed:
                if posLocation[s[beg]][0] < st:
                    isValid = False
                    break
                ed = max(posLocation[s[beg]][1], ed)
                beg += 1
            if isValid:
                setResult.add((st, ed))
        setResult = list(setResult)
        setResult.sort(key=lambda x: x[1])
        result = []
        prevEnd = -1
        for st, ed in setResult:
            if st > prevEnd:
                result.append(s[st:ed+1])
                prevEnd = ed
        return result