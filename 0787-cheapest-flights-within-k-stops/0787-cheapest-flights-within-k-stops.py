class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        g=[[] for _ in range(n)]

        for fromi,toi,pricei in flights:
            g[fromi].append((toi,pricei))
        stop=[0]*n
        hp=[(0,-(k+1),src)]

        while hp:
            d,k,u=heapq.heappop(hp)

            if u==dst:return d
            k=abs(k)
            if k<=stop[u] or k==0:continue
            stop[u]=k

            for v,w in g[u]:
                heapq.heappush(hp,(w+d,-(k-1),v))
        return -1




        