class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        next=[i+1 for i in range(n)]
        dis=n-1
        ans=[]

        for u,v in queries:
            curr=next[u]

            while curr<v:
                dis-=1
                temp=next[curr]
                next[curr]=v
                curr=temp

            next[u]=max(next[u],v)
            ans.append(dis)

        return ans