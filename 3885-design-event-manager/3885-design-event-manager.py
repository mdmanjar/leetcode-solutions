import heapq

class node:
    def __init__(self, id, p):
        self.id = id
        self.p = p
        self.active = True

    def __lt__(self, other):
        if self.p != other.p:
            return self.p > other.p
        return self.id < other.id

class EventManager:
    def __init__(self, events: list[list[int]]):
        self.hp = []
        self.mp = {}

        for id, pr in events:
            x = node(id, pr)
            self.mp[id] = x
            heapq.heappush(self.hp, x)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        if eventId in self.mp:
            self.mp[eventId].active = False
            x = node(eventId, newPriority)
            self.mp[eventId] = x
            heapq.heappush(self.hp, x)

    def pollHighest(self) -> int:
        while self.hp and not self.hp[0].active:
            heapq.heappop(self.hp)

        if self.hp:
            id = heapq.heappop(self.hp).id
            del self.mp[id]
            return id
        return -1