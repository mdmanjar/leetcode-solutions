class Solution:
    fact=[1]*10

    for i in range(1,10):
        fact[i]=i*fact[i-1]

    def isDigitorialPermutation(self,n:int)->bool:
        sm=0
        temp=n

        while temp:
            sm+=self.fact[temp%10]
            temp//=10

        count=[0]*10

        while n:
            count[n%10]+=1
            n//=10

        while sm:
            count[sm%10]-=1
            sm//=10

        return all(x==0 for x in count)