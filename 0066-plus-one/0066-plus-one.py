class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1,-1,-1):
            if nums[i]<9:
                nums[i]+=1
                return nums
            nums[i]=0
        
        nums[0]=1
        nums.append(0)
        return nums
        