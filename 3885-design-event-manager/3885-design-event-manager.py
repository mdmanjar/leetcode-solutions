import heapq

class Node:
    def __init__(self, id: int, p: int):
        self.id = id
        self.priority = p
        self.active = True

    # Python's heapq is a min-heap by default.
    # To mimic Java's max-heap (highest priority first, then smallest id):
    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority > other.priority
        return self.id < other.id

class EventManager:
    def __init__(self, events: list[list[int]]):
        self.pq = []
        self.mp = {}

        for x in events:
            node = Node(x[0], x[1])
            heapq.heappush(self.pq, node)
            self.mp[x[0]] = node

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        if eventId in self.mp:
            self.mp[eventId].active = False
            node = Node(eventId, newPriority)
            self.mp[eventId] = node
            heapq.heappush(self.pq, node)

    def pollHighest(self) -> int:
        while self.pq and not self.pq[0].active:
            heapq.heappop(self.pq)
            
        if not self.pq:
            return -1
            
        return heapq.heappop(self.pq).id