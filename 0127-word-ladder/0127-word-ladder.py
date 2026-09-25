class Solution:
    def ladderLength(self,beginWord,endWord,wordList):
        words=set(wordList)

        if endWord not in words:return 0

        parents=defaultdict(list)
        queue=deque([beginWord])
        visited={beginWord}
        found=False
        level=1

        while queue and not found:
            level_visited=set()

            for _ in range(len(queue)):
                word=queue.popleft()
                x=list(word)

                for i in range(len(x)):
                    old=x[i]

                    for j in range(26):
                        c=chr(j+97)

                        if c==old:continue

                        x[i]=c
                        nxt=''.join(x)

                        if nxt in words and nxt not in visited:
                            if nxt not in level_visited:
                                queue.append(nxt)
                                level_visited.add(nxt)

                            parents[nxt].append(word)

                            if nxt==endWord:
                                found=True

                    x[i]=old

            if found:return level+1

            visited.update(level_visited)
            level+=1

        return 0

