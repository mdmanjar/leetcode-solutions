class event:

    def __init__(self,id,priority):
        self.id=id
        self.priority=priority
        self.live=True
    def __lt__(self,other):
        if self.priority!=other.priority:
            return self.priority>other.priority
        return self.id<other.id
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.hp=[]
        self.mp={}
        for id ,priority in events:
            x=event(id,priority)
            self.hp.append(x)
            self.mp[id]=x
        heapq.heapify(self.hp)
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        if eventId in self.mp:
            self.mp[eventId].live=False
        x=event(eventId,newPriority)
        self.mp[eventId]=x
        heapq.heappush(self.hp,x)
        
    def pollHighest(self) -> int:

        while self.hp and not self.hp[0].live:
            heapq.heappop(self.hp)
        if not self.hp:return -1
        x=heapq.heappop(self.hp)
        del self.mp[x.id]
        return x.id
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()