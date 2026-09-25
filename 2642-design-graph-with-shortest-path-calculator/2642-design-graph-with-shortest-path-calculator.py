class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g=[[] for _ in range(n)]

        for u,v,w in edges:
            self.g[u].append((v,w)) 
        

    def addEdge(self, edge: List[int]) -> None:
        u,v,w=edge
        self.g[u].append((v,w))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        n=len(self.g)
        dist=[inf]*n
        dist[node1]=0

        hp=[(0,node1)]

        while hp:
            d,u=heapq.heappop(hp)

            if u==node2:return d
            if d>dist[u]:continue

            for v,w in self.g[u]:
                nd=d+w
                if nd<dist[v]:
                    dist[v]=nd
                    heapq.heappush(hp,(nd,v))
        
        return -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)