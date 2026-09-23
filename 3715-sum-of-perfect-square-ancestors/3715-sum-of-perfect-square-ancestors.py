def square_free(n):
    ans=1
    p=2

    while p*p<=n:
        cnt=0
        while n%p==0:
            n//=p
            cnt+=1
        if cnt%2!=0:
            ans*=p
        p+=1

    if n>1:
        ans*=n

    return ans



class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
      for i in range(n):nums[i]=square_free(nums[i])
      # print(nums)
      g=[[] for _ in range(n)]
      for u,v in edges:
        g[u].append(v)
        g[v].append(u)

      mp=defaultdict(int)
      def dfs(u,p):
        ans=mp[nums[u]]
        mp[nums[u]]+=1

        for v in g[u]:
          if v!=p:ans+=dfs(v,u)
        mp[nums[u]]-=1
        if mp[nums[u]]==0:
            del mp[nums[u]]
        return ans
      return dfs(0,-1)

