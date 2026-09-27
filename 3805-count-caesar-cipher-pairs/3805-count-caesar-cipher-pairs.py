class Solution:
    def countPairs(self, words: List[str]) -> int:
        mp=defaultdict(int)
        ans=0

        for word in words:
            cnt=[0]*26
            for c in word:cnt[((ord(c)-97)-ord(word[0])-97)%26]+=1
            x=tuple(cnt)
            ans+=mp[x]
            mp[x]+=1
        return ans

        
        