class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        mp=[0]*26
        ans=[]

        for i,c in enumerate(min(strs)):
            for word in strs:
                mp[ord(word[i])-97]+=1
            if mp[ord(c)-97]!=len(strs):
                break
            mp[ord(c)-97]=0
            ans.append(c)

        return ''.join(ans)
        