class Solution:
    def generatePossibleNextMoves(self, current_state: str) -> list[str]:
        return [
            current_state[:i] + '--' + current_state[i+2:] 
            for i in range(len(current_state) - 1) 
            if current_state[i:i+2] == '++'
        ]