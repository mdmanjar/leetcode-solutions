class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq=deque()
        n=len(nums)
        ans=[]

        for i,e in enumerate(nums):

            while dq and nums[dq[-1]]<e:
                dq.pop()

            dq.append(i)

            if i+1>=k:

                ans.append(nums[dq[0]])

                if i-dq[0]+1>=k:
                    dq.popleft()
        return ans
        