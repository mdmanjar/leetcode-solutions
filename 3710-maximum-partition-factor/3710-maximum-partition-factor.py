
class Solution:
    def maxPartitionFactor(self,points):
        n=len(points)

        if n<=2:
            return 0

        dist=[[0]*n for _ in range(n)]
        mx=0

        for i in range(n):
            for j in range(i+1,n):
                dist[i][j]=dist[j][i]=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                mx=max(mx,dist[i][j])

        def find(x):
            if parent[x]<0:
                return x
            parent[x]=find(parent[x])
            return parent[x]

        def union(a,b):
            a=find(a)
            b=find(b)
            if a==b:
                return
            if parent[a]>parent[b]:
                a,b=b,a
            parent[a]+=parent[b]
            parent[b]=a
        parent=None
        def possible(target):
            nonlocal parent
            parent=[-1]*(2*n)

            for i in range(n):
                for j in range(i+1,n):
                    if dist[i][j]>=target:
                        continue

                    if find(i)==find(j):
                        return False

                    union(i,j+n)
                    union(i+n,j)

            return True

        low=0
        high=mx
        ans=-1

        while low<=high:
            mid=low+(high-low)//2

            if possible(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1

        return ans
