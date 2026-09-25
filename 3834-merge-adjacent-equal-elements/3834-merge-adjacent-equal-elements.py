class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack=[]

        for e in nums:

            while stack and stack[-1]==e:
                e=stack.pop()+e
            stack.append(e)
        return stack

        