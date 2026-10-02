class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        pos=[e for e in nums if e>=0]
        neg=[-e for e in nums if e<0]

        def radix_sort(nums):
            if not nums:return []
            mx=max(nums)
            i=1
            while i<=mx:
                count_sort(i,nums)
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
            nums[:]=temp

        pos=radix_sort(pos)
        neg=radix_sort(neg)

        return [-e for e in neg[::-1]]+pos