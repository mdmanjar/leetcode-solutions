class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx=deque()
        mn=deque()
        ans=0
        left=0

        for right ,e in enumerate(nums):

            while mn and nums[mn[-1]]>e:mn.pop()
            while mx and nums[mx[-1]]<e:mx.pop()

            mn.append(right)
            mx.append(right)

            while (nums[mx[0]]-nums[mn[0]])*(right-left+1)>k:
                if mn[0]==left:mn.popleft()
                if mx[0]==left:mx.popleft()
                left+=1
            ans+=right-left+1
        return ans


        