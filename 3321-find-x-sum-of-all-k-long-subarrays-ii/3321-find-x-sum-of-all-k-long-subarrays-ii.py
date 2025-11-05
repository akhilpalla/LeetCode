class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k == 0 or n < k:
            return []
        answer = []
        freq = defaultdict(int)
        entry_map = {}  
        top_set = SortedList()
        rest_set = SortedList()
        sum_x = 0
        window_sum = sum(nums[:k])
        for val in nums[:k]:
            freq[val] += 1
        for val in freq:
            entry = (-freq[val], -val)
            rest_set.add(entry)
            entry_map[val] = {'entry': entry, 'set': 'rest'}
        while len(top_set) < x and rest_set:
            entry = rest_set.pop(0)
            val = -entry[1]
            top_set.add(entry)
            entry_map[val]['set'] = 'top'
            sum_x += freq[val] * val
        for i in range(n - k + 1):
            if len(freq) <= x:
                answer.append(window_sum)
            else:
                answer.append(sum_x)
            if i + k >= n:
                break
            left_val = nums[i]
            right_val = nums[i + k]
            old_freq = freq[left_val]
            if old_freq > 0:
                data = entry_map.get(left_val)
                if data:
                    current_entry = data['entry']
                    if data['set'] == 'top':
                        top_set.discard(current_entry)
                        sum_x -= old_freq * left_val
                    else:
                        rest_set.discard(current_entry)
                    del entry_map[left_val]
                new_freq = old_freq - 1
                if new_freq > 0:
                    new_entry = (-new_freq, -left_val)
                    rest_set.add(new_entry)
                    entry_map[left_val] = {'entry': new_entry, 'set': 'rest'}
                    freq[left_val] = new_freq
                else:
                    del freq[left_val]
            old_freq_r = freq.get(right_val, 0)
            if right_val in entry_map:
                data = entry_map[right_val]
                current_entry = data['entry']
                if data['set'] == 'top':
                    top_set.discard(current_entry)
                    sum_x -= old_freq_r * right_val
                else:
                    rest_set.discard(current_entry)
                del entry_map[right_val]
            new_freq_r = old_freq_r + 1
            new_entry_r = (-new_freq_r, -right_val)
            rest_set.add(new_entry_r)
            entry_map[right_val] = {'entry': new_entry_r, 'set': 'rest'}
            freq[right_val] = new_freq_r
            while len(top_set) < x and rest_set:
                entry = rest_set.pop(0)
                val = -entry[1]
                top_set.add(entry)
                entry_map[val]['set'] = 'top'
                sum_x += freq[val] * val
            while len(top_set) > x:
                entry = top_set.pop(-1)
                val = -entry[1]
                rest_set.add(entry)
                entry_map[val]['set'] = 'rest'
                sum_x -= freq[val] * val
            while top_set and rest_set and rest_set[0] < top_set[-1]:
                removed_entry = top_set.pop(-1)
                rest_set.add(removed_entry)
                val = -removed_entry[1]
                entry_map[val]['set'] = 'rest'
                sum_x -= freq[val] * val
                added_entry = rest_set.pop(0)
                top_set.add(added_entry)
                val = -added_entry[1]
                entry_map[val]['set'] = 'top'
                sum_x += freq[val] * val
            window_sum = window_sum - left_val + right_val
        return answer