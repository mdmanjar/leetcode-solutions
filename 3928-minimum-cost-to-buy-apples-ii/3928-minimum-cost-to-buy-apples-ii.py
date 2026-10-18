class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        g=[[] for _ in range(n)]

        for u,v,c,t in roads:
            g[u].append((v,c,t))
            g[v].append((u,c,t))
        
        def without_apple(src,price):
            dist=[inf]*n
            dist[src]=0
            hp=[(0,src)]

            while hp:
                cost,u=heapq.heappop(hp)

                if cost!=dist[u]:continue

                for v,c,_ in g[u]:
                    new_c=c+cost
                    if new_c<dist[v] and new_c<price:
                        dist[v]=new_c
                        heapq.heappush(hp,(new_c,v))
            return dist

        def with_apple(src,x,price):
            dist=[inf]*n
            dist[src]=0
            hp=[(0,src)]

            while hp:
                cost,u=heapq.heappop(hp)

                if cost!=dist[u]:continue
                price=min(price,x[u]+cost+prices[u])
                for v,c,t in g[u]:
                    new_cost=cost+(c*t)
                    if new_cost<dist[v] and new_cost<price:
                        dist[v]=new_cost
                        heapq.heappush(hp,(new_cost,v))
            return price
        ans=[]
        for i in range(n):
            x=without_apple(i,prices[i])
            ans.append(with_apple(i,x,prices[i]))
        return ans
        

               

        
        
