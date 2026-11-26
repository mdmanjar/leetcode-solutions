class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums=self.sortArray(nums)
        ans=0
        for i in range(1,len(nums)):
            ans=max(ans,nums[i]-nums[i-1])
        return ans
    def sortArray(self, nums: list[int]) -> list[int]:
        pos=[e for e in nums if e>=0]
        neg=[-e for e in nums if e<0]

        def sort(nums):
            if len(nums)==0:return nums
            mx,i=max(nums),1

            while i<=mx:
                nums=count_sort(nums,i)
                i*=10
            return nums

        def count_sort(nums,d):
            count=[0]*10

            for e in nums:
                count[(e//d)%10]+=1

            count=list(accumulate(count))
            temp=[0]*len(nums)

            for e in nums[::-1]:
                idx=count[(e//d)%10]-1
                temp[idx]=e
                count[(e//d)%10]-=1
            return temp
        pos=sort(pos)
        neg=sort(neg)
        return [-e for e in neg[::-1]]+pos
        