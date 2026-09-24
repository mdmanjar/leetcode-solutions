class Solution:
    def stringIndices(self, words: List[str], queries: List[str]) -> List[int]:
        root={}
        mn=min(range(len(words)),key=lambda i:len(words[i]))
        root[0]=mn

        for i,word in enumerate(words):
            cur=root
            for c in reversed(word):
                cur=cur.setdefault(c,{})
                cur[0]=min(cur.get(0,i),i,key=lambda x:len(words[x]))

        ans=[]
        for q in queries:
            cur=root
            idx=root[0]

            for c in reversed(q):
                if c not in cur:
                    break
                cur=cur[c]
                idx=cur[0]

            ans.append(idx)

        return ans