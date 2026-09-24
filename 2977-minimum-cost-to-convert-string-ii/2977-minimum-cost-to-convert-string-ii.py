class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        id={}
        uq_id=0

        for word in original:
            if word not in id:
                id[word]=uq_id
                uq_id+=1

        for word in changed:
            if word not in id:
                id[word]=uq_id
                uq_id+=1

        n=uq_id
        dist=[[inf]*n for _ in range(n)]

        for i in range(n):
            dist[i][i]=0

        for a,b,c in zip(original,changed,cost):
            dist[id[a]][id[b]]=min(dist[id[a]][id[b]],c)

        for k in range(n):
            for i in range(n):
                if dist[i][k]==inf:continue
                for j in range(n):
                    if dist[k][j]!=inf:
                        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

        lengths=set(map(len,original))

        @cache
        def dfs(i):
            if i==len(source):return 0

            ans=inf

            if source[i]==target[i]:
                ans=dfs(i+1)

            for l in lengths:
                j=i+l
                if j>len(source):continue

                x=source[i:j]
                y=target[i:j]

                if x in id and y in id and dist[id[x]][id[y]]!=inf:
                    z=dfs(j)
                    if z!=inf:
                        ans=min(ans,z+dist[id[x]][id[y]])

            return ans

        ans=dfs(0)
        return -1 if ans==inf else ans