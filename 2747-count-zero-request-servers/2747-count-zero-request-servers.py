class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs = sorted(logs, key=lambda log: log[1])
        ordered_queries = sorted(
            (time, index) for index, time in enumerate(queries)
        )
        requests = [0] * (n + 1)
        answer = [0] * len(queries)
        active_servers = 0
        left = right = 0

        for time, index in ordered_queries:
            # Add requests at or before the query time.
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]

                if requests[server] == 0:
                    active_servers += 1

                requests[server] += 1
                right += 1

            # Remove requests strictly before the window starts.
            while left < right and logs[left][1] < time - x:
                server = logs[left][0]
                requests[server] -= 1

                if requests[server] == 0:
                    active_servers -= 1

                left += 1

            answer[index] = n - active_servers

        return answer