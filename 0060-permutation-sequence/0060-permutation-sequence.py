class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=list(range(1,n+1))
        ans=[]

        fact=1
        for i in range(1,n):
            fact*=i

        k-=1
        used=0

        while used<len(nums):
            i=k//fact
            ans.append(nums.pop(i))
            if not nums:
                break
            k%=fact
            fact//=len(nums)

        return ''.join(map(str,ans))