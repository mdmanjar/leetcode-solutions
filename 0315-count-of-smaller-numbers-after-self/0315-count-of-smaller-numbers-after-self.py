
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        nums=[(e,i) for i,e in enumerate(nums)]
        n=len(nums)
        count=[0]*n


        def divide(left,right):
            if left>=right:return
            mid=left+(right-left)//2
            divide(left,mid)
            divide(mid+1,right)
            merge(left,mid,right)

        def merge(left,mid,right):
            temp=[]
            i=left
            j=mid+1

            while i<=mid and j<=right:
                if nums[i][0]>nums[j][0]:
                    count[nums[i][1]]+=right-j+1
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            nums[left:right+1]=temp+nums[i:mid+1]+nums[j:right+1]
        divide(0,len(nums)-1)

        return count