class Solution:
    def reversePairs(self, nums: list[int]) -> int:


        def merge(left,mid,right):
            i,j=left,mid+1
            ans=0
            while i<=mid:
                while j<=right and not (nums[i]>2*nums[j]):
                    j+=1
                if j>right:break
                ans+=right-j+1
                i+=1

            i,j=left,mid+1

            temp=[]

            while i<=mid and j<=right:

                if nums[i]>nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            nums[left:right+1]=temp+nums[i:mid+1]+nums[j:right+1]
            return ans

        def divide(left,right):
            if left>=right:return 0
            mid=left+(right-left)//2
            return divide(left,mid)+divide(mid+1,right)+merge(left,mid,right)

        return divide(0,len(nums)-1)