class Solution:
    def generateCombinations(self, index, current_path, letter_map, digits, results):
        # If the current path length matches the length of digits, a combination is complete
        if len(current_path) == len(digits):
            results.append("".join(current_path))
            return  # Backtrack

        # Retrieve the letters corresponding to the current digit and iterate through them
        possible_chars = letter_map[digits[index]]
        for char in possible_chars:
            # Add the current character to the current path
            current_path.append(char)
            # Proceed to the next digit
            self.generateCombinations(index + 1, current_path, letter_map, digits, results)
            # Backtrack by removing the last added character
            current_path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        results = []
        self.generateCombinations(0, [], letter_map, digits, results)
        return results
# T = 4^n * N, 4^n because what is input is 777999 it has 4 ways, multiply by N because we have to build the ans string
# ASC = N