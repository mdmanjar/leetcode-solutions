class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        n=len(nums)

        p=[-1]*n

        def find(a):
            if p[a]<0:return a
            p[a]=find(p[a])
            return p[a]

        def union(a,b):
            a,b=find(a),find(b)
            if a==b:return
            if p[a]>p[b]:a,b=b,a
            p[a]+=p[b]
            p[b]=a

        mp={}

        def prime_factor(x,i):
          d=2
          while d*d<=x:
            if x%d==0:
              if d in mp:union(i,mp[d])
              else:mp[d]=i
              while x%d==0:x//=d
            d+=1
          if x>1:
            if x in mp:union(i,mp[x])
            else:mp[x]=i

        for i,e in enumerate(nums):prime_factor(e,i)

        return -min(p)
        