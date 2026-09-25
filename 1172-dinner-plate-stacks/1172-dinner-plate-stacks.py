import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hp=[]
        self.stack=[]
        self.inhp=set()

    def push(self, val: int) -> None:
        while self.hp and (self.hp[0]>=len(self.stack) or len(self.stack[self.hp[0]])==self.capacity):
            idx=heapq.heappop(self.hp)
            self.inhp.discard(idx)

        if self.hp:
            idx=self.hp[0]
        else:
            idx=len(self.stack)
            self.stack.append([])

        self.stack[idx].append(val)

        if len(self.stack[idx])==self.capacity:
            if idx in self.inhp:
                self.inhp.remove(idx)
                heapq.heappop(self.hp)
        elif idx not in self.inhp:
            heapq.heappush(self.hp,idx)
            self.inhp.add(idx)

    def pop(self) -> int:
        while self.stack and not self.stack[-1]:
            idx=len(self.stack)-1
            self.stack.pop()
            self.inhp.discard(idx)

        if not self.stack:
            self.hp=[]
            self.inhp.clear()
            return -1

        idx=len(self.stack)-1
        v=self.stack[idx].pop()

        if idx not in self.inhp:
            heapq.heappush(self.hp,idx)
            self.inhp.add(idx)

        return v

    def popAtStack(self, index: int) -> int:
        if index<0 or index>=len(self.stack) or not self.stack[index]:
            return -1

        v=self.stack[index].pop()

        if index not in self.inhp:
            heapq.heappush(self.hp,index)
            self.inhp.add(index)

        return v