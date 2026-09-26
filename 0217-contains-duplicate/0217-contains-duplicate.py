class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq=set()

        for e in nums:
            if e in uniq:
                return True
            uniq.add(e)
        return False
        