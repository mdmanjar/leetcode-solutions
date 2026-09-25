class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        n=len(passingFees)
        g=[[] for _ in range(n)]

        for u,v,t in edges:
            g[u].append((v,t))
            g[v].append((u,t))

        fees=[[inf]*(maxTime+1) for _ in range(n)]
        fees[0][0]=passingFees[0]
        hp=[(passingFees[0],0,0)]

        while hp:
            fee,t,u=heapq.heappop(hp)

            if fee!=fees[u][t]:
                continue

            if u==n-1:
                return fee

            for v,tm in g[u]:
                nt=t+tm

                if nt>maxTime:
                    continue

                nf=fee+passingFees[v]

                if nf<fees[v][nt]:
                    fees[v][nt]=nf
                    heapq.heappush(hp,(nf,nt,v))

        return -1