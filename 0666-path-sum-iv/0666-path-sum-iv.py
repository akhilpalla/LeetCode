class Solution:
    def single_path_sum(self, level_map, parents_map, leaf_depth, leaf_idx):
        # find single path sum from leaf upto root
        cur_depth = leaf_depth
        cur_idx = leaf_idx
        single_path_sum = 0
        while (cur_depth, cur_idx) in parents_map:
            single_path_sum += level_map[cur_depth][cur_idx]
            parent_depth, parent_idx = parents_map[(cur_depth, cur_idx)]
            cur_depth = parent_depth
            cur_idx = parent_idx

        # also add the value of root
        return single_path_sum + level_map[cur_depth][cur_idx]

    def construct_parents_map(self, level_map, root_idx):
        parents_map = {}
        leaf_pos = []
        # idx, depth
        queue = deque([(root_idx, 1)])

        # BFS
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                front = queue.popleft()
                front_idx, depth = front

                is_leaf = True
                if (depth + 1) in level_map:
                    # left child: 2 * idx - 1
                    left_idx = front_idx * 2 
                    next_level = level_map[depth + 1]
                    if left_idx < len(next_level) and next_level[left_idx] != -1:
                        is_leaf = False
                        parents_map[(depth + 1, left_idx)] = (depth, front_idx)
                        queue.append((left_idx, depth + 1))

                    # right child: 2 * idx 
                    right_idx = front_idx * 2 + 1
                    if right_idx < len(next_level) and next_level[right_idx] != -1:
                        is_leaf = False
                        parents_map[(depth + 1, right_idx)] = (depth, front_idx)
                        queue.append((right_idx, depth + 1))

                if is_leaf:
                    leaf_pos.append((depth, front_idx))

        return parents_map, leaf_pos

    def pathSum(self, nums: List[int]) -> int:
        level_map = {}
        root_idx = 0
        for num in nums:
            depth = num // 100
            position = (num % 100) // 10
            value = (num % 100) % 10
            if depth not in level_map:
                curr_exp = depth - 1
                level_map[depth] = [-1] * (2**curr_exp)
            level_map[depth][position - 1] = value
            
        path_sum = 0
        # calculate sum of all paths from the root towards the leaves.
        # first get the map from leaves upto the root and also the leaf positions
        parents_map, leaf_pos = self.construct_parents_map(level_map, root_idx)
        for (leaf_depth, leaf_idx) in leaf_pos:
            if level_map[leaf_depth][leaf_idx] != -1:
                path_sum += self.single_path_sum(level_map, parents_map, leaf_depth, leaf_idx)
        
        return path_sum