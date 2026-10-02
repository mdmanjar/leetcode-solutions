class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def radix_sort(nums):
            if not nums:
                return []
            mx=max(nums)
            i=1
            while i<=mx:
                nums=count_sort(i,nums)
                i*=10
            return nums

        def count_sort(i,nums):
            count=[0]*10
            for e in nums:count[(e//i)%10]+=1
            count=list(accumulate(count))

            temp=[0]*len(nums)

            for e in nums[::-1]:
                idx=(e//i)%10
                temp[count[idx]-1]=e
                count[idx]-=1
            return temp
        nums=radix_sort(nums)
        ans=0

        for i in range(1,len(nums)):
            ans=max(ans,nums[i]-nums[i-1])

        return ans
        