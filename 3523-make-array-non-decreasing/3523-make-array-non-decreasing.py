class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        top=0

        for e in nums[1:]:
            if nums[top]<=e:
                top+=1
                nums[top]=e

        return top+1
        