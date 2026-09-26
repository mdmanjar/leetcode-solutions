class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        c1=Counter(nums1)
        c2=Counter(nums2)
        ans=[]

        for e in nums1:
            if e in c1 and e in c2:
                ans.extend([e]*min(c1[e],c2[e]))
                del c1[e]
                del c2[e]

        return ans