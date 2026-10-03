class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.mp = {}

    def add(self, node: Node) -> None:
        """Appends a node to the end (most recently used position)."""
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
        self.mp[node.key] = node

    def __delitem__(self, node: Node) -> None:
        """Enables `del dll_instance[node]` syntax."""
        if node.key not in self.mp:
            return
        self.size -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.mp[node.key]

    def __len__(self) -> int:
        return self.size

    def __contains__(self, key: int) -> bool:
        return key in self.mp

    def __getitem__(self, key: int):
        return self.mp.get(key)

    def last(self) -> Node:
        """Returns the least recently used node (node after dummy head)."""
        return self.head.next if self.size > 0 else None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = DLL()

    def get(self, key: int) -> int:
        node = self.items[key]
        if not node:
            return -1
        # Move node to the back (most recently used)
        del self.items[node]
        self.items.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.items[key]
        if node:
            # Key exists: update value and move to back
            node.val = value
            del self.items[node]
            self.items.add(node)
        else:
            # Key does not exist: create and add new node
            new_node = Node(key, value)
            self.items.add(new_node)
            # Evict least recently used item if over capacity
            if len(self.items) > self.capacity:
                lru_node = self.items.last()
                if lru_node:
                    del self.items[lru_node]