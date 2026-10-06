class node:

    def __init__(self, key=-1, freq=0, value=0):
        self.key = key
        self.freq = freq
        self.value = value
        self.prev = None
        self.next = None


class dll:

    def __init__(self):
        self.head = node()
        self.tail = node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def apppend(self, new_node):
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

        self.size += 1

    def __delitem__(self, deleted_node):
        deleted_node.prev.next = deleted_node.next
        deleted_node.next.prev = deleted_node.prev

        self.size -= 1

    def pop(self):
        deleted_node = self.tail.prev
        self.__delitem__(deleted_node)
        return deleted_node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.freq = {}
        self.min_freq = 0

    def update(self, old_node):

        f = old_node.freq

        self.freq[f].__delitem__(old_node)

        if self.freq[f].size == 0:
            del self.freq[f]

            if self.min_freq == f:
                self.min_freq += 1

        old_node.freq += 1

        if old_node.freq not in self.freq:
            self.freq[old_node.freq] = dll()

        self.freq[old_node.freq].apppend(old_node)

    def get(self, key: int) -> int:

        if key not in self.mp:
            return -1

        old_node = self.mp[key]

        self.update(old_node)

        return old_node.value

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.mp:

            old_node = self.mp[key]
            old_node.value = value

            self.update(old_node)

            return

        if len(self.mp) == self.capacity:

            old_node = self.freq[self.min_freq].pop()

            del self.mp[old_node.key]

            if self.freq[self.min_freq].size == 0:
                del self.freq[self.min_freq]

        new_node = node(key, 1, value)

        if 1 not in self.freq:
            self.freq[1] = dll()

        self.freq[1].apppend(new_node)

        self.mp[key] = new_node
        self.min_freq = 1