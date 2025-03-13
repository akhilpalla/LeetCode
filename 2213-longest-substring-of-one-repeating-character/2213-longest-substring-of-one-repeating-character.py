from sortedcontainers import SortedList
class Solution:
    def longestRepeating(self, s: str, qc: str, qi):
        qr = list(zip(list(qc), qi))
        srt = SortedList([])
        mx = SortedList([])
        cr = s[0]
        sz = 1
        start, end = 0, 0
        for i in range(1, len(s)):
            if s[i] == cr:
                sz += 1
                end = i
            else:
                srt.add((start, end, sz, cr))
                mx.add(sz)
                cr = s[i]
                start = i
                end = i
                sz = 1
        srt.add((start, end, sz, cr))
        mx.add(sz)
        s = list(s)
        n = len(s)
        ans = [0] * len(qr)
        for id, (ch, ind) in enumerate(qr):
            if s[ind] == ch:
                ans[id] = mx[-1]
                continue
            s[ind] = ch

            ll = srt.bisect_left((ind, n + 1, n + 1, "z")) - 1
            start, end, sz, cho = srt[ll]
            srt.pop(ll)
            # todo start==end
            if start == end:

                mx.remove(sz)
                if ind + 1 < n and s[ind + 1] == ch and ind - 1 >= 0 and s[ind - 1] == ch:
                    ll = srt.bisect_left((ind + 1, n + 1, n + 1, "z")) - 1
                    sr, endr, szr, chr = srt[ll]
                    srt.pop(ll)
                    mx.remove(szr)
                    ll = srt.bisect_left((ind - 1, n + 1, n + 1, "z")) - 1
                    sl, endl, szl, chl = srt[ll]
                    srt.pop(ll)
                    mx.remove(szl)
                    mid = (sl, endr, szr+szl+1, ch)
                    srt.add(mid)
                    mx.add(szr+szl+1)
                elif ind + 1 < n and s[ind + 1] == ch:
                    ll = srt.bisect_left((ind + 1, n + 1, n + 1, "z")) - 1
                    sr, endr, szr, chr = srt[ll]
                    srt.pop(ll)
                    right = (ind, endr, szr + 1, chr)
                    srt.add(right)
                    mx.remove(szr)
                    mx.add(szr + 1)
                elif ind - 1 >= 0 and s[ind - 1] == ch:
                    ll = srt.bisect_left((ind - 1, n + 1, n + 1, "z")) - 1
                    sl, endl, szl, chl = srt[ll]
                    srt.pop(ll)
                    left = (sl, ind, szl + 1, ch)
                    srt.add(left)
                    mx.remove(szl)
                    mx.add(szl + 1)
                else:
                    srt.add((start, end, sz, ch))
                    mx.add(sz)

            elif ind == end:
                left = (start, end - 1, sz - 1, cho)
                srt.add(left)
                mx.remove(sz)
                mx.add(sz - 1)
                if ind + 1 < n and s[ind + 1] == ch:
                    ll = srt.bisect_left((ind + 1, n + 1, n + 1, "z")) - 1
                    sr, endr, szr, chr = srt[ll]
                    srt.pop(ll)
                    right = (ind, endr, szr + 1, chr)
                    srt.add(right)
                    mx.remove(szr)
                    mx.add(szr + 1)
                else:
                    right = (ind, ind, 1, ch)
                    srt.add(right)
                    mx.add(1)
            elif ind == start:
                right = (start + 1, end, sz - 1, cho)
                srt.add(right)
                mx.remove(sz)
                mx.add(sz-1)
                if ind - 1 >= 0 and s[ind - 1] == ch:
                    ll = srt.bisect_left((ind - 1, n + 1, n + 1, "z")) - 1
                    sl, endl, szl, chl = srt[ll]
                    srt.pop(ll)
                    left = (sl, ind, szl + 1, ch)
                    mx.remove(szl)
                    srt.add(left)
                    mx.add(szl + 1)
                else:
                    left = (ind, ind, 1, ch)
                    srt.add(left)
                    mx.add(1)
            else:
                left = (start, ind - 1, ((ind - 1)-start + 1), cho)
                mid = (ind, ind, 1, ch)
                right = (ind + 1, end, (end - (ind + 1) +1), cho)
                srt.add(left)
                srt.add(right)
                srt.add(mid)
                mx.remove(sz)
                mx.add(left[2])
                mx.add(right[2])
                mx.add(1)

            ans[id] = mx[-1]
        return ans