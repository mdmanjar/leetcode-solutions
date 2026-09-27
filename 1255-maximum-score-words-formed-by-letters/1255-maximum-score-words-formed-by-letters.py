from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq=[0]*26

        for c in letters:
            freq[ord(c)-97]+=1
        
        def dfs(i):
            if i==len(words):return 0
            max_score=0
            complete=True

            for c in words[i]:
                idx=ord(c)-97
                freq[idx]-=1
                max_score+=score[idx]

                if freq[idx]<0:
                    complete=False
            x=0
            if complete:
                x=dfs(i+1)+max_score
            for c in words[i]:
                freq[ord(c)-97]+=1
            return max(x,dfs(i+1))
        return dfs(0)