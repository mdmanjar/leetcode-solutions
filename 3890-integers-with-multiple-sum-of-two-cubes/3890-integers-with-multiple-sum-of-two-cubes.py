class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        mp=defaultdict(int)

        def cube(n):
            low=1
            high=n
            while low<high:
                mid=low+(high-low)//2
                x=mid**3
                if x<=n:
                    low=mid+1
                else:
                    high=mid
            return low
        x=cube(n)
        
        for i in range(1,x):
            for j in range(i+1,x):
                y=i**3+j**3
                if y>n:break
                mp[y]+=1
        ans=[k for k,v in mp.items() if v>=2]
        return sorted(ans)


        