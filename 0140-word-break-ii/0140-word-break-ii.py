class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root={}

        def add(word):
            t=root

            for c in word:t=t.setdefault(c,{})
            t['#']=word

        for word in wordDict:add(word)


        def dfs(i):

            if i==len(s):
                ans.append(' '.join(temp))
                return

            t=root
            j=i

            while i<len(s):

                if s[i] not in t:break

                t=t[s[i]]

                if '#' in t :
                    temp.append(t['#'])
                    dfs(i+1)
                    temp.pop()

                i+=1

        ans=[]
        temp=[]
        dfs(0)
        return ans