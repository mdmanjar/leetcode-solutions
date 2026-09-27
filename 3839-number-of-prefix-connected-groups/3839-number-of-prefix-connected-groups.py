class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        mp=defaultdict(int)

        for word in words:
            if len(word)>=k:
                mp[word[:k]]+=1
        
        return sum(1 for v in mp.values() if v>1)