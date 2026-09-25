class Solution:
    def componentValue(self, nums: list[int], edges: list[list[int]]) -> int:
        n=len(nums)
        g=[[] for _ in range(n)]

        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        total=sum(nums)

        for components in range(n,0,-1):
            if total%components:continue

            target=total//components

            def dfs(u,p):
                sm=nums[u]

                for v in g[u]:
                    if v==p:continue
                    x=dfs(v,u)

                    if x>target:
                        return x

                    sm+=x

                if sm>target:
                    return sm
                if sm==target:
                    return 0

                return sm

            if dfs(0,-1)==0:
                return components-1

        return 0