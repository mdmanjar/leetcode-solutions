class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        root={}

        def add(word):
            t=root
            for c in word:
                t=t.setdefault(c,{})
                t['#']=t.get('#',0)+1

        def cal(word):
            t=root
            ans=0

            for c in word:
                t=t[c]
                ans+=t['#']
            return ans
        
        for word in words:add(word)

        return [cal(word)  for word in words]

            

        