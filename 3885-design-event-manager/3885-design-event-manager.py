import heapq

class Event:
    def __init__(self, id, priority):
        self.id = id
        self.priority = priority
        self.live = True

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority > other.priority
        return self.id < other.id

class EventManager:

    def __init__(self, events: list[list[int]]):
        self.hp = []
        self.mp = {}
        for id, priority in events:
            x = Event(id, priority)
            self.hp.append(x)
            self.mp[id] = x
        heapq.heapify(self.hp)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        if eventId in self.mp:
            # Mark the old event instance as dead
            self.mp[eventId].live = False
        
        # Create and push the new updated event
        x = Event(eventId, newPriority)
        self.mp[eventId] = x
        heapq.heappush(self.hp, x)

    def pollHighest(self) -> int:
        # Clean up any dead events at the top of the heap
        while self.hp and not self.hp[0].live:
            heapq.heappop(self.hp)
            
        if not self.hp:
            return -1
            
        x = heapq.heappop(self.hp)
        del self.mp[x.id]
        return x.id