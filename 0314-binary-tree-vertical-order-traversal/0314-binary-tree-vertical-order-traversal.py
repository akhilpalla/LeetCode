#In this question if there are multiple at same column we will follow level order
#in 987 we will follow sorted order

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
import sys

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        col_map = defaultdict(list)  # Map to store nodes based on their column index
        node_queue = deque([(root, 0)])  # Queue for BFS traversal with (node, column) pairs
        max_col, min_col = -sys.maxsize, sys.maxsize  # Track the range of column indices

        # Perform BFS traversal
        while node_queue:
            curr_node, col_index = node_queue.popleft()

            if curr_node:
                max_col = max(max_col, col_index)
                min_col = min(min_col, col_index)
                col_map[col_index].append(curr_node.val)  # Group node values by column

                # Enqueue the left and right children with updated column indices
                node_queue.append((curr_node.left, col_index - 1))
                node_queue.append((curr_node.right, col_index + 1))

        result = []
        # Collect the nodes in column order from min_col to max_col
        for col in range(min_col, max_col + 1):
            # if col in col_map:
            result.append(col_map[col])

        return result
  

# T = S = N