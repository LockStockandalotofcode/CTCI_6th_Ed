class Node:

    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Dictionary: Map key to node

        # Dummy nodes for boundary handling
        # Left = LRU, Right = MRU
        # Most Recently Used (MRU) and Least Recently Used (LRU).
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Helper to put() to remove node from doubly linked list
    def remove(self, node):
        prev,nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        
    # Insert node at right as MRU
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # update MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        # otherwise
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists update its value, otherwise add the key, value pair to cache
        if key in self.cache:
            self.remove(self.cache[key])

        # Add new node to cache dictionary and list
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove LRU from list and delete from Map(cache dictionary)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)