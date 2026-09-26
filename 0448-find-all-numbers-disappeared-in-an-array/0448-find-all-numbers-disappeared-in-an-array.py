class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for e in nums:
            e=abs(e)-1
            nums[e]=-abs(nums[e])
        return [ i+1 for i in range(len(nums)) if nums[i]>0]
        
        