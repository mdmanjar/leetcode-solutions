class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        g=[[] for _ in range(n)]

        for u,v,cost,tax in roads:
            g[u].append((v,cost,tax))
            g[v].append((u,cost,tax))
        
        def without_apples(src,limit):
            dist=[math.inf]*n
            dist[src]=0
            hp=[(0,src)]


            while hp:
                d,u=heapq.heappop(hp)
                if d!=dist[u]:continue
                for v,w,_ in g[u]:
                    nd=w+d
                    if nd<dist[v] and nd<limit:
                        dist[v]=nd
                        heapq.heappush(hp,(nd,v))
            return dist

        def with_apples(src,limit,without_apple):
            dist=[math.inf]*n
            dist[src]=0
            hp=[(0,src)]

            while hp:
                d,u=heapq.heappop(hp)
                if d!=dist[u]:continue
                limit=min(limit,without_apple[u]+d+prices[u])
                for v,w,tax in g[u]:
                    nd=d+(w*tax)
                    if nd<limit and nd<dist[v]:
                        dist[v]=nd
                        heapq.heappush(hp,(nd,v))
            return limit
        
        return [with_apples(i,prices[i],without_apples(i,prices[i])) for i in range(n)]
            

        