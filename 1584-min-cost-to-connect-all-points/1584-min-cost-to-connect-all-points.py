class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        p=[-1]*n

        def find(a):
            if p[a]<0:return a
            p[a]=find(p[a])
            return p[a]

        def union(a,b):
            if (a:=find(a))==(b:=find(b)):return False
            p[b]=a
            return True

        return sum(c for i, j, c in sorted(((i, j, abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])) for i in range(n-1) for j in range(i+1, n)), key=lambda x: x[2]) if union(i, j))