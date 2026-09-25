class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:return []
        n=len(wordList)

        words=set(wordList)

        q=deque([beginWord])

        visited=set()

        g=defaultdict(list)
        endFound=True

        while q and endFound:
            level=set()

            for _ in range(len(q)):
                cur_word=q.popleft()
                cur=list(cur_word)

                for i in range(len(cur)):
                    old_chr=cur[i]

                    for c in string.ascii_lowercase:
                        if old_chr==c:continue

                        cur[i]=c
                        x=''.join(cur)

                        if x in words and x not in visited:
                            g[x].append(cur_word)
                            if x not in level:
                                level.add(x)
                                q.append(x)
                            if x==endWord:
                                endFound=False

                    cur[i]=old_chr
            visited|=level

        if endFound:return []

        ans = []
        temp = [endWord]


        def dfs(word):
            if word == beginWord:
                ans.append(temp[::-1])
                return

            for parent in g[word]:
                temp.append(parent)
                dfs(parent)
                temp.pop()


        dfs(endWord)

        return ans