import collections

#using level order

class Solution:
    def connect(self, root: "Node") -> "Node":
        # If the tree is empty, return None
        if not root:
            return root

        # Initialize a queue to perform level-order traversal
        q = collections.deque([root])

        # While there are still nodes to process
        while q:

            level_size = len(q)  # Get the number of nodes at the current level

            # Process all nodes at the current level
            for i in range(level_size):

                current_node = q.popleft()  # Get the next node in the queue

                # If this is not the last node at the current level, 
                # connect it to the next node in the queue
                #q[0] because after popping the element its right will be at the top of queue
                if i < level_size - 1:
                    current_node.next = q[0]

                # Add the left and right children of the current node to the queue
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)

        # Return the root node after all connections are made
        return root

# T = S = N

#+++++===TRICK BY USING ALREADY ESTABLISHED LINK================
class Solution:
    def connect(self, root: "Node") -> "Node":

        # If the root is None, return None
        if not root:
            return root

        # Start with the root node, which is the leftmost node at the first level
        level_start = root

        # Traverse levels until we reach the last level where leftmost nodes do not exist
        while level_start.left:

            # Use a pointer to iterate through nodes at the current level
            current_node = level_start
            while current_node:

                # Link the left child to the right child (CONNECTION 1)
                current_node.left.next = current_node.right

                # If there is a next node, link right child to the next node's left child (CONNECTION 2)
                if current_node.next:
                    current_node.right.next = current_node.next.left

                # Move to the next node at the same level
                current_node = current_node.next

            # Move down to the next level, starting from the leftmost node
            level_start = level_start.left

        # Return the root node with next pointers properly connected
        return root

# T = N
# S = 1