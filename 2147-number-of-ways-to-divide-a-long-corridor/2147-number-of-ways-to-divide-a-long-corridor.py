class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        MODULO = 10**9 + 7

        segments = []
        curr_seat_count = 0
        marker = 0

        for i, x in enumerate(corridor):
            if x == 'S':
                curr_seat_count += 1
                if curr_seat_count == 1:
                    marker = i
                elif curr_seat_count == 2:
                    segments.append((marker, i))
                    curr_seat_count = 0

        if curr_seat_count != 0 or len(segments) == 0:
            return 0
        if len(segments) == 1:
            return 1

        ans = 1
        for i in range(1, len(segments)):
            choices = segments[i][0] - segments[i - 1][1]
            ans = (ans * choices) % MODULO

        return ans