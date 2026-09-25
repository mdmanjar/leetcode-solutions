
class Node:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node("", -1)
        self.tail = Node("", -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def __len__(self):
        return self.size

    def recentUsed(self):
        return self.head.next.key


class AllOne:

    def __init__(self):
        self.stack = [DLL()]  # stack[0] is unused
        self.hp = []
        self.mp = {}

    def inc(self, key: str) -> None:

        if key in self.mp:
            x = self.mp[key]

            self.stack[x.freq].remove(x)
            x.freq += 1

        else:
            x = Node(key, 1)
            self.mp[key] = x

        idx = x.freq

        while len(self.stack) <= idx: # 1
            self.stack.append(DLL())

        self.stack[idx].add(x)

        heapq.heappush(self.hp, idx)

    def dec(self, key: str) -> None:

        x = self.mp[key]
        idx = x.freq

        self.stack[idx].remove(x)

        if len(self.stack[-1])==0:
            self.stack.pop()

        idx -= 1

        if idx == 0:
            del self.mp[key]
            return

        x.freq = idx
        self.stack[idx].add(x)

        heapq.heappush(self.hp, idx)

    def getMaxKey(self) -> str:
        return  self.stack[-1].recentUsed() if len(self.stack)>1 else""

    def getMinKey(self) -> str:

        while self.hp:
            idx = self.hp[0]

            if idx < len(self.stack) and len(self.stack[idx]) > 0:
                return self.stack[idx].recentUsed()

            heapq.heappop(self.hp)

        return ""