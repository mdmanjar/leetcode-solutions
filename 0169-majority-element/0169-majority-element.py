class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        x=-inf
        count=1

        for c in nums:
            if x!=c:
                count-=1
                if count==0:
                    x=c
                    count=1
            else:
                count+=1
        return x

                
        