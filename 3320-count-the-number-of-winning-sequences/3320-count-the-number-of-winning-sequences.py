MODULE = 10**9 + 7
class Solution:
    relation_map = {
        "F": {"W": 1, "F": 0, "E": -1},
        "W": {"W": 0, "F": -1, "E": 1},
        "E": {"W": -1, "F": 1, "E": 0},
    }
    def countWinningSequences(self, s: str) -> int:
        discard_bar = -len(s) / 2
        last_round = {
            "F": {self.score(s[0], "F"): 1},
            "W": {self.score(s[0], "W"): 1},
            "E": {self.score(s[0], "E"): 1},
        }
        moves = ["F", "W", "E"]
        for curr_round_num in range(1, len(s)):
            new_round = {"F": Counter(), "W": Counter(), "E": Counter()}
            alice_move = s[curr_round_num]
            for bob_move in moves:
                bob_score = self.score(alice_move, bob_move)
                for last_move in moves:
                    if last_move != bob_move:
                        for score_count in last_round[last_move].items():
                            if score_count[0] + bob_score > discard_bar:
                                new_round[bob_move][score_count[0] + bob_score] = (
                                    score_count[1]
                                    + new_round[bob_move][score_count[0] + bob_score]
                                ) % MODULE
            last_round = new_round
        total = 0
        for last_counts in last_round.values():
            for item in last_counts.items():
                if item[0] > 0:
                    total = (total + item[1]) % MODULE
        return total
    def score(self, alice, bob):
        return self.relation_map[alice][bob]