class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack=[0]

        for e in nums:
            if stack[-1]<=e:stack.append(e)
        return len(stack)-1
        