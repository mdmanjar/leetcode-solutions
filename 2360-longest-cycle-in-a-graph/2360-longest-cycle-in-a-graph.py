
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        vst=[None]*n
        time=[0]*n
        ans=-1
        def dfs(u,t):
            nonlocal ans
            if vst[u] is not None:
                if vst[u] is False:
                    ans=max(ans,t-time[u])
                return
            vst[u]=False

            time[u]=t
            if edges[u]!=-1:
                dfs(edges[u],t+1)
            vst[u]=True

        for i in range(n):
            dfs(i,0)

        return ans