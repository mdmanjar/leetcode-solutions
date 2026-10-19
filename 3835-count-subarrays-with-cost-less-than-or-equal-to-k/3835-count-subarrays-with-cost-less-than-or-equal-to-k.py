class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx=deque()
        mn=deque()
        left=0

        ans=0


        for right in range(len(nums)):
            e=nums[right]
            while mn and nums[mn[-1]]>e:
                mn.pop()
            
            while mx and nums[mx[-1]]<e:
                mx.pop()

            mn.append(right)
            mx.append(right)

            while mn and mx and (nums[mx[0]]-nums[mn[0]])*(right-left+1)>k:
                if mn[0]==left:
                    mn.popleft()
                if mx[0]==right:
                    mx.popleft()
                left+=1
            
            ans+=(right-left+1)
        return ans
        