class Solution:
    def countPairs(self, words: List[str]) -> int:
        mp=defaultdict(int)
        ans=0

        for word in words:
            p=ord(word[0])-97
            temp=[]
            for c in word:
                i=ord(c)-97
                temp.append(chr((i-p+26)%26+97))
            x=''.join(temp)
            ans+=mp[x]
            mp[x]+=1
        return ans

        
        