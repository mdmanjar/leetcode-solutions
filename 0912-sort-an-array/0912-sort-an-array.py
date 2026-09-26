class Solution:
    def sortArray(self, nums):
        neg=[-x for x in nums if x<0]
        pos=[x for x in nums if x>=0]

        def radix_sort(nums):
            if not nums:return nums
            mx=max(nums)

            def count_sort(x):
                count=[0]*10

                for e in nums:
                    count[(e//x)%10]+=1

                for i in range(1,10):
                    count[i]+=count[i-1]

                ans=[0]*len(nums)

                for i in range(len(nums)-1,-1,-1):
                    d=(nums[i]//x)%10
                    idx=count[d]-1
                    ans[idx]=nums[i]
                    count[d]-=1

                nums[:]=ans

            x=1
            while mx//x:
                count_sort(x)
                x*=10

            return nums

        radix_sort(neg)
        radix_sort(pos)

        return [-x for x in reversed(neg)]+pos