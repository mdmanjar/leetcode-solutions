class FreqStack:

    def __init__(self):
        self.mp=defaultdict(lambda:-1)
        self.stack=[]
    def push(self, val: int) -> None:
        self.mp[val]+=1
        idx=self.mp[val]
        if idx==len(self.stack):
            self.stack.append([])
        self.stack[idx].append(val)

    def pop(self) -> int:
        v=self.stack[-1].pop()
        if not self.stack[-1]:self.stack.pop()
        self.mp[v]-=1
        if self.mp[v]==-1:
            del self.mp[v]
        return v
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()