class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def divid(left,right):
            nonlocal nums
            if left>=right:return
            mid=left+(right-left)//2
            divid(left,mid)
            divid(mid+1,right)

            i,j=left,mid+1
            temp=[]
            while i<=mid and j<=right:
                if nums[i]<nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            
            nums[left:right+1]=temp+nums[i:mid+1]+nums[j:right+1]
        
        divid(0,len(nums)-1)
        return nums
        