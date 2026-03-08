
class LogSystem:
    import bisect
    def __init__(self):
        self.stk = []

    def put(self, id: int, timestamp: str) -> None:
        bisect.insort(self.stk, (timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        granularity_to_index = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }
        idx = granularity_to_index[granularity]
        start_prefix = start[:idx]
        end_prefix = end[:idx]
        min_timestamp = {
            "Year": ":01:01:00:00:00",
            "Month": ":01:00:00:00",
            "Day": ":00:00:00",
            "Hour": ":00:00",
            "Minute": ":00",
            "Second": ""
        }
        max_timestamp = {
            "Year": ":12:31:23:59:59",
            "Month": ":31:23:59:59",
            "Day": ":23:59:59",
            "Hour": ":59:59",
            "Minute": ":59",
            "Second": ""
        }
        start_cmp = start_prefix + min_timestamp[granularity]
        end_cmp = end_prefix + max_timestamp[granularity]
        i = bisect.bisect_left(self.stk, (start_cmp, 0))
        j = bisect.bisect_right(self.stk, (end_cmp, float('inf')))
        res = [id for _, id in self.stk[i:j]]
        return res



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)