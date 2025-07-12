class Solution:
    def earliestAndLatest(self, n: int, first: int, second: int) -> List[int]:
        first -= 1
        second -= 1

        @cache
        def process_round(current_round, remaining_players):
            players_in_round = deque()
            for player in range(n):
                if remaining_players & (1 << player):
                    players_in_round.append(player)

            possible_matchups = []
            while len(players_in_round) > 1:
                p1, p2 = players_in_round.popleft(), players_in_round.pop()
                if (p1 == first and p2 == second) or (p1 == second and p2 == first):
                    return [current_round, current_round]
                if p1 in (first, second):
                    possible_matchups.append([p2])
                elif p2 in (first, second):
                    possible_matchups.append([p1])
                else:
                    possible_matchups.append([p1, p2])

            min_round, max_round = float('inf'), -float('inf')
            for match in product(*possible_matchups):
                updated_mask = remaining_players
                for winner in match:
                    updated_mask ^= 1 << winner
                min_r, max_r = process_round(current_round + 1, updated_mask)
                min_round = min(min_round, min_r)
                max_round = max(max_round, max_r)

            return min_round, max_round

        return process_round(1, (1 << n) - 1)