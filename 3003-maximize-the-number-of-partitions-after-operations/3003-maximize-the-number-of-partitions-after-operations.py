class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k == 26 or k > len(set(s)):  return 1
        if k == 1:
            mx, cur, cnt, prev = 0, 0, -1, ''
            for c in s:
                if c == prev:
                    cur += 1
                else:
                    mx = max(mx, cur)
                    cur, prev = 1, c
                    cnt += 1
            mx = max(mx, cur)
            return cnt + min(mx, 3)
        n, s = len(s), [1 << ord(c)-97 for c in s]
        suff1, suff2, setMap, inds = [0]*n, [0]*n, [0]*n, {1<<i: n for i in range(26)}
        set1, cnt1, par1, ptr1 = 0, 0, 1, n-1
        set2, cnt2, par2, ptr2 = 0, 0, 1, n-1
        for i in range(n-1,-1,-1):
            suff2[i], setMap[i] = par2, set1
            if not set2 & s[i]:
                if cnt2 == k-1:
                    while ptr2 > inds[s[ptr2]]:    ptr2 -= 1
                    par2 = suff1[ptr2] + 1
                    set2 ^= s[ptr2]
                    ptr2 -= 1
                    cnt2 -= 1
                set2 |= s[i]
                cnt2 += 1
            if not set1 & s[i]:
                if cnt1 == k:
                    while ptr1 > inds[s[ptr1]]:    ptr1 -= 1
                    par1 = suff1[ptr1] + 1
                    set1 ^= s[ptr1]
                    ptr1 -= 1
                    cnt1 -= 1
                set1 |= s[i]
                cnt1 += 1
            suff1[i], inds[s[i]] = par1, i
        res = suff1[0]
        mode1, mode2 = False, False
        set0, cnt0, par0, mask = 0, 0, 1, (1<<26)-1
        for i in range(n):
            if not set0 & s[i]:
                if cnt0 == k-1:
                    if mode1:
                        res = max(res, par0 + suff1[i])
                    mode2 = True
                elif cnt0 == k:
                    mode1, mode2 = False, False
                    set0, cnt0 = 0, 0
                    par0 += 1
                set0 |= s[i]
                cnt0 += 1
            elif mode2:
                if set0 | setMap[i] < mask:
                    res = max(res, par0 + suff2[i])
                else:
                    res = max(res, par0 + suff1[i])
                mode2 = False
            elif not mode1:
                mode1 = True
        return res