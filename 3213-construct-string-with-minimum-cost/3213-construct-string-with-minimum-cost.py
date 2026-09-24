class Solution:
    class Node:
        def __init__(self):
            self.children=[None]*26
            self.fail=None
            self.last=None
            self.len=0
            self.cost=float('inf')

    class AhoCorasick:
        def __init__(self):
            self.root=Solution.Node()

        def put(self,s,cost):
            cur=self.root

            for c in s:
                i=ord(c)-97
                if cur.children[i] is None:
                    cur.children[i]=Solution.Node()
                cur=cur.children[i]

            cur.len=len(s)
            cur.cost=min(cur.cost,cost)

        def buildFail(self):
            root=self.root
            root.fail=root
            root.last=root

            q=deque()

            for i in range(26):
                child=root.children[i]

                if child is None:
                    root.children[i]=root
                else:
                    child.fail=root
                    child.last=root
                    q.append(child)

            while q:
                cur=q.popleft()

                for i in range(26):
                    child=cur.children[i]

                    if child is None:
                        cur.children[i]=cur.fail.children[i]
                        continue

                    child.fail=cur.fail.children[i]

                    if child.fail.len>0:
                        child.last=child.fail
                    else:
                        child.last=child.fail.last

                    q.append(child)

    def minimumCost(self,target: str,words: List[str],costs: List[int]) -> int:
        ac=self.AhoCorasick()

        for word,cost in zip(words,costs):
            ac.put(word,cost)

        ac.buildFail()

        n=len(target)
        INF=10**18
        dp=[INF]*(n+1)
        dp[0]=0

        cur=ac.root

        for i in range(1,n+1):
            cur=cur.children[ord(target[i-1])-97]

            if cur.len>0:
                dp[i]=min(dp[i],dp[i-cur.len]+cur.cost)

            match=cur.last

            while match!=ac.root:
                dp[i]=min(
                    dp[i],
                    dp[i-match.len]+match.cost
                )
                match=match.last

        return -1 if dp[n]==INF else dp[n]