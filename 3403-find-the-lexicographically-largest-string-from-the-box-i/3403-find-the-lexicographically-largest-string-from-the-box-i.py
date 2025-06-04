class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        large_letter = 'a'
        large_index = -1
        indices = []
        for ind, char in enumerate(word):
            if char > large_letter:
                large_letter = char
                large_index = ind
                indices.append(ind)
            elif char == large_letter:
                indices.append(ind)

        answer = "a"
        for ind in indices:
            end_index = ind + (len(word) - numFriends)
            if end_index > len(word) - 1:
                if word[ind: ] > answer:
                    answer = word[ind:]
            else:
                if word[ind : end_index + 1] > answer:
                    answer = word[ind : end_index + 1]
        return answer