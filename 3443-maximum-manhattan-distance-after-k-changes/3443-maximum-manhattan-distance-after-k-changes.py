class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        log = defaultdict(int)
        inverts = {
            "N": "S",
            "S": "N",
            "E": "W",
            "W": "E"
        }

        ans = 0
        for i in s:
            log[i] += 1
            max_x = "N" if log["N"] >= log["S"] else "S"
            max_y = "E" if log["E"] >= log["W"] else "W"

            local = log[max_x] + log[max_y]
            ins = log[inverts[max_x]] + log[inverts[max_y]] 
            ops_used = min(k, ins)
            local += ops_used
            local -= ins - ops_used
            ans = max(ans, local)
        return ans