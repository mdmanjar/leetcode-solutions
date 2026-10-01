class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        p=[-1]*n

        def find(a):
            if p[a]<0:return a
            p[a]=find(p[a])
            return p[a]
        
        def union(a,b):
            a,b=find(a),find(b)
            if a==b:return
            if p[a]>p[b]:a,b=b,a
            p[a]+=p[b]
            p[b]=a
        for i in range(1,n):
            if nums[i]-nums[i-1]<=maxDiff:
                union(i-1,i)
        return [find(a)==find(b) for a,b in queries]
        