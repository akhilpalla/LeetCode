class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int: 
        cols = len(picture[0])

        compressed = []
        res = 0
        for r in picture:
            compressed += r
        curr = 0
        last_seen_at_idx = -1
        i = 0

        while i < len(compressed):

            curr_window_end = i + (cols - i % cols)
            if compressed[i] == "B" and i < curr_window_end:
                curr += 1
                last_seen_at_idx = i

                if curr > 1:
                    i = curr_window_end
                    curr = 0
                    last_seen_at_idx = -1

            if i == curr_window_end - 1 and curr == 1:
                j, k = last_seen_at_idx, last_seen_at_idx
                seen_b = False
                
                while j >= 0 or k < len(compressed):
                    j -= cols
                    k += cols
                    if (
                        k < len(compressed)
                        and compressed[k] == "B"
                        or j >= 0
                        and compressed[j] == "B"
                    ):
                        seen_b = True
                        break
                if not seen_b:
                    res += 1

                curr = 0
                last_seen_at_idx = -1

            i += 1

        return res