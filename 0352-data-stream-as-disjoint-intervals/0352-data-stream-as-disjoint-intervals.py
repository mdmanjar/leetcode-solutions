class dsu:
    def __init__(self,n):
        self.p=[None]*n
        self.mp={}
    
    def find(self,a):
        if self.p[a]<0:return a
        self.p[a]=self.find(self.p[a])
        return self.p[a]
    
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        self.mp[a]=(self.mp[a][0],self.mp[b][1])
        del self.mp[b]
        self.p[b]=a
    def add(self,i):
        if self.p[i] is not None:return
        self.p[i]=-1
        self.mp[i]=(i,i)

        if i>0 and self.p[i-1] is not None:
            self.union(i-1,i)

        if i+1<len(self.p) and self.p[i+1] is not None:
            self.union(i,i+1)
    def intervals(self):
        return sorted(self.mp.values())

class SummaryRanges:

    def __init__(self):
        self.uf=dsu(10001)
        

    def addNum(self, value: int) -> None:
        self.uf.add(value)
        

    def getIntervals(self) -> list[list[int]]:
        return self.uf.intervals()
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()