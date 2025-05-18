class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        index_mapping = {word: i for i, word in enumerate(words)}
        adj_list = [[] for _ in range(len(words))]
        for word in words:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    if i == 0:
                        new_word = c + word[1:]
                    elif i == len(word) - 1:
                        new_word = word[:i] + c
                    else:
                        new_word = word[:i] + c + word[i+1:]
                    if new_word in index_mapping:
                        curr_idx = index_mapping[word]
                        new_idx = index_mapping[new_word]
                        if new_idx > curr_idx and groups[new_idx] != groups[curr_idx]:
                            adj_list[curr_idx].append(new_idx)

        new_visit = [-1] * len(words)
        prev_length = 0
        prev_ans = []

        queue = deque()

        for i in range(len(words)):
            if new_visit[i] == 1:
                continue
            temp_list = [i]
            queue.append((1, temp_list))
            while queue:
                curr_size, lst = queue.pop()
                curr_ele = lst[-1]
                if new_visit[curr_ele] > curr_size:
                    if curr_size > prev_length:
                        prev_length = curr_size
                        prev_ans = lst
                    continue
                flag = False
                for neighbor in adj_list[curr_ele]:
                    if groups[neighbor] != groups[curr_ele] and new_visit[neighbor] < curr_size + 1:
                        new_list = lst[:]
                        new_list.append(neighbor)
                        queue.append((curr_size + 1, new_list))
                        flag = True
                if not flag:
                    if curr_size > prev_length:
                        prev_length = curr_size
                        prev_ans = lst
                    continue
                new_visit[curr_ele] = curr_size

        final_ans = [words[i] for i in prev_ans]
        return final_ans