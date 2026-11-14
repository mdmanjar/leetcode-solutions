class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        mp=[None]*26

        for word in wordDict:
            idx=ord(word[0])-97
            mp[idx]=(word,mp[idx])
        
        ans=[]
        temp=[]

        def dfs(i):
            if len(s)==i:
                ans.append(' '.join(temp))
                return
            idx=ord(s[i])-97
            node=mp[idx]

            while node:
                word,next=node
                node=next
                if s.startswith(word,i):
                    temp.append(word)
                    dfs(i+len(word))
                    temp.pop()
        dfs(0)

        return ans
        