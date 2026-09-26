class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans=[]

        for i,c in enumerate(min(strs)):
            count=0
            for word in strs:
                if word[i]==c:count+=1
                else:break
            if count!=len(strs):
                break
            ans.append(c)

        return ''.join(ans)
        