class dsu:
    def __init__(self,p):
        self.p=p[:]

    def find(self,a):
        if self.p[a]<0:return a
        self.p[a]=self.find(self.p[a])
        return self.p[a]

    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b:return False
        if self.p[a]>self.p[b]:
            a,b=b,a
        self.p[a]+=self.p[b]
        self.p[b]=a
        return True


class Solution:
    def maxStability(self,n:int,edges:List[List[int]],k:int)->int:
        optional=[]
        mx=math.inf
        must=0
        base=dsu([-1]*n)
        rem=n-1

        for u,v,s,m in edges:
            if m:
                if not base.union(u,v):return -1
                mx=min(mx,s)
                must+=1
                rem-=1
            else:
                optional.append((u,v,s))

        if rem==0:return mx

        def check(x):
            uf=dsu(base.p)
            cnt=0
            upgrade=0

            for u,v,s in optional:
                if s>=x:
                    if uf.union(u,v):
                        cnt+=1

            for u,v,s in optional:
                if s<x and s*2>=x:
                    if uf.union(u,v):
                        cnt+=1
                        upgrade+=1
                        if upgrade>k:
                            return False

            return cnt==rem

        left=0
        right=2*max(s for _,_,s,_ in edges)
        ans=-1

        while left<=right:
            mid=(left+right)//2
            if mid<=mx and check(mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1

        return ans