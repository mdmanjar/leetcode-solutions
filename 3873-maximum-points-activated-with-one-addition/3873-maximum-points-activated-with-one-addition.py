class dsu:
    def __init__(self,n):
        self.p=[-1]*n
        self.cmp=n
    
    def find(self,a):
        if self.p[a]<0:return a
        self.p[a]=self.find(self.p[a])
        return self.p[a]
    
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b:return
        if self.p[a]>self.p[b]:a,b=b,a
        self.p[a]+=self.p[b]
        self.p[b]=a
        self.cmp-=1
    
    def size(self,a):
        return -self.p[self.find(a)]

class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        mpx={}
        mpy={}
        n=len(points)
        uf=dsu(n)

        for i,(x,y) in enumerate(points):
            if x in mpx:
                uf.union(i,mpx[x])
            else:
                mpx[x]=i

            if y in mpy:
                uf.union(i,mpy[y])
            else:
                mpy[y]=i

        if uf.cmp==1:
            return n+1

        mx=0
        smx=0

        for i in range(n):
            if uf.p[i]<0:
                sz=uf.size(i)
                if sz>mx:
                    smx=mx
                    mx=sz
                elif sz>smx:
                    smx=sz

        return mx+smx+1