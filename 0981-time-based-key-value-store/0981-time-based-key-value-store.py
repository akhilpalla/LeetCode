"""
problem: what's the most recent value stored at time stored_timestamp <= timestamp?

set: appending is amortized O(1)
get: O(log m) where m is the count for that key. bisect_right uses binary search
"""


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, k: str, v: str, set_t: int) -> None:
        self.map[k].append((set_t, v))

    def get(self, k: str, t: int) -> str:
        if k not in self.map:
            return ""
        arr = self.map[k]

        # bisect_right gives first index AFTER t. so one before is the most RECENT entry before t
        # key lambda makes comparison against time only. this makes it so that if there's an entry at exactly time t
        # bisect_right returns one after, but then minus one, to pick that entry.
        most_recent_prev_time = bisect_right(arr, t, key=lambda p: p[0]) - 1
        if most_recent_prev_time == -1:
            return ""
        return arr[most_recent_prev_time][1]