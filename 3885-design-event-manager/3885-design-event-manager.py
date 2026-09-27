class node:
    def __init__(self,id,priority):
        self.id=id
        self.priority=priority
        self.active=True

    def __lt__(self,other):
        if self.priority!=other.priority:
            return self.priority>other.priority
        return self.id<other.id

class EventManager:

    def __init__(self, events: list[list[int]]):
        self.hp=[]
        self.mp={}
        for id ,priority in events:
            x=node(id,priority)
            self.hp.append(x)
            self.mp[id]=x

        heapq.heapify(self.hp)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        if eventId in self.mp:
            self.mp[eventId].active=False
        x=node(eventId,newPriority)
        self.mp[eventId]=x
        heapq.heappush(self.hp,x)


    def pollHighest(self) -> int:
        while self.hp and not self.hp[0].active:
            heapq.heappop(self.hp)
        if self.hp:
          return heapq.heappop(self.hp).id
        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()