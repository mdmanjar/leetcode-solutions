class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        st=set()

        for i,e in enumerate(nums):
            if e in st:return True
            st.add(e)
            if i+1>k:
                st.discard(nums[i-k])
        return False
            
        