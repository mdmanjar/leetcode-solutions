class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        mp=[0]*26
        left=0


        for right in range(len(s)):
            mp[ord(s[right])-ord('A')]+=1
            mx=max(mp)
            while k<right-left+1-mx:
                mp[ord(s[left])-65]-=1
                left+=1


            ans=max(ans,right-left+1)

        return ans

        