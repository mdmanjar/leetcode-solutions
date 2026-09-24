class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        p=[-1]*n

        def find(a):
            if p[a]<0:
                return a
            p[a]=find(p[a])
            return p[a]

        def union(a,b):
            a,b=find(a),find(b)
            if a==b:return
            if p[a]>p[b]:
                a,b=b,a
            p[a]+=p[b]
            p[b]=a

        mp={}
        for i,x in enumerate(nums):
            if x in mp:
                union(i,mp[x])
            else:
                mp[x]=i

        owner=[-1]*(threshold+1)

        for x,i in mp.items():
            if x>threshold:
                continue

            for m in range(x,threshold+1,x):
                if owner[m]==-1:
                    owner[m]=i
                else:
                    union(i,owner[m])

        return sum(p[i]<0 for i in range(n))