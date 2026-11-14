class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        # mp=[None]*26

        # for word in wordDict:
        #     idx=ord(word[0])-97
        #     mp[idx]=(word,mp[idx])
        
        # ans=[]
        # temp=[]

        # def dfs(i):
        #     if len(s)==i:
        #         ans.append(' '.join(temp))
        #         return
        #     idx=ord(s[i])-97
        #     node=mp[idx]

        #     while node:
        #         word,next=node
        #         node=next
        #         if s.startswith(word,i):
        #             temp.append(word)
        #             dfs(i+len(word))
        #             temp.pop()
        # dfs(0)

        # return ans

        ans=[]
        temp=[]
        root={}

        for word in wordDict:
            t=root

            for c in word:
                t=t.setdefault(c,{})
            t['#']=word
        
        def dfs(r,i):
            if len(s)==i:
                if '#' in r:
                    temp.append(r['#'])
                    ans.append(' '.join(temp))
                    temp.pop()
                return
            if '#' in r:
                temp.append(r['#'])
                dfs(root,i)
                temp.pop()
            if s[i] in r:
                dfs(r[s[i]],i+1)
        dfs(root,0)
        return ans
            

    
        