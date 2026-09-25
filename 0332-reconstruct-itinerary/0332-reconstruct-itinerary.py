class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)

        for u,v in tickets:
            graph[u].append(v)
        
        for v in graph.values():heapq.heapify(v)
        ans=[]
        def dfs(u):
            while graph[u]:dfs(heapq.heappop(graph[u]))
            ans.append(u)
        dfs('JFK')

        return ans[::-1]

        