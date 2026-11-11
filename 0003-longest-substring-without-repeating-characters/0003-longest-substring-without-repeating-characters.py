class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp=[False]*128
        left=0
        ans=0

        for i in range(len(s)):

            while mp[ord(s[i])]:
                mp[ord(s[left])]=False
                left+=1
            ans=max(ans,i-left+1)
            mp[ord(s[i])]=True
        return ans
            
        