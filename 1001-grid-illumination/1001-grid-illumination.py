class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        rows=defaultdict(int)
        cols=defaultdict(int)
        d1=defaultdict(int)
        d2=defaultdict(int)
        lamps=set((r,c) for r,c in lamps)

        for r,c in lamps:
            rows[r]+=1
            cols[c]+=1
            d1[r+c]+=1
            d2[r-c]+=1
        dir=((0,0),(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1))
        ans=[]

        for r,c in queries:
            if rows[r] or cols[c] or d1[r+c] or d2[r-c]:
                ans.append(1)
                for x,y in dir:
                    u,v=x+r,c+y
                    if -1<u<n and -1<v<n and (u,v) in lamps:
                        lamps.discard((u,v))
                        rows[u]-=1
                        cols[v]-=1
                        d1[u+v]-=1
                        d2[u-v]-=1
            else:
                ans.append(0)
        return ans


        