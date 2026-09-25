class Solution:
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[-1]*n
        stack=[]
        stack1=[]

        for i,e in enumerate(nums):
            while stack1 and nums[stack1[-1]]<e:
                ans[stack1.pop()]=e
            temp=[]

            while stack and nums[stack[-1]]<e:
                temp.append(stack.pop())
            
            while temp:
                stack1.append(temp.pop())
            stack.append(i)
        return ans
        

        