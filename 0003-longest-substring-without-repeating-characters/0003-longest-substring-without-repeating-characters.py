class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp=[-1]*128
        left=0
        ans=0

        for i,e in enumerate(s):
            left=max(left,mp[ord(e)]+1)
            ans=max(ans,i-left+1)
            mp[ord(e)]=i
        return ans
        


        