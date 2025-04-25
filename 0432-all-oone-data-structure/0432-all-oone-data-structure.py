# Cracking Faang
class Node:
    def __init__(self, freq):
        self.freq = freq        # Frequency count for this node
        self.prev = None        # Previous node in doubly-linked list
        self.next = None        # Next node in doubly-linked list
        self.keys = set()       # Set of keys that have this frequency

class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.char_map = {}

        
    def inc(self, key: str) -> None:
        if key in self.char_map:
            node = self.char_map[key]
            freq = node.freq
            node.keys.remove(key)
            
            next_node = node.next
            
            if next_node == self.tail or next_node.freq != freq + 1:
                new_node = Node(freq + 1)
                new_node.keys.add(key)
                
                new_node.prev = node
                new_node.next = next_node
                node.next = new_node
                next_node.prev = new_node
                
                self.char_map[key] = new_node
            else:
                next_node.keys.add(key)
                self.char_map[key] = next_node
                
            if not node.keys:
                self.removeNode(node)

        else:
            first_node = self.head.next
            
            if first_node == self.tail or first_node.freq > 1:
                new_node = Node(1)
                new_node.keys.add(key)
                
                new_node.prev = self.head
                new_node.next = first_node
                self.head.next = new_node
                first_node.prev = new_node
                
                self.char_map[key] = new_node
            else:
                first_node.keys.add(key)
                self.char_map[key] = first_node
        

    def dec(self, key: str) -> None:
        # Return if key doesn't exist
        if key not in self.char_map:
            return
            
        # Get current node and remove key from it
        node = self.char_map[key]
        node.keys.remove(key)
        
        freq = node.freq
        
        # If frequency is 1, remove the key entirely
        if freq == 1:
            del self.char_map[key]
        else:
            prev_node = node.prev
            
            # Check if we need to create a new node with freq-1
            if prev_node == self.head or prev_node.freq != freq - 1:
                new_node = Node(freq - 1)
                new_node.keys.add(key)
                
                # Insert new node before current node
                new_node.prev = prev_node
                new_node.next = node
                prev_node.next = new_node
                node.prev = new_node
                
                self.char_map[key] = new_node
            else:
                # Add to existing node with freq-1
                prev_node.keys.add(key)
                self.char_map[key] = prev_node
        
        # Remove the old node if it's empty
        if not node.keys:
            self.removeNode(node)
        

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        else:
            return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        else:
            return next(iter(self.head.next.keys))

    def removeNode(self, node):
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()