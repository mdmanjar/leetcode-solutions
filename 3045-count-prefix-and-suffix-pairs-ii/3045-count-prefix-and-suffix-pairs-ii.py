class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        mp=[[None]*26 for _ in range(26)]
        freq=defaultdict(int)

        def add(word):
            if word in freq:
                freq[word]+=1
                return
            freq[word]+=1
            p=ord(word[0])-97
            s=ord(word[-1])-97
            mp[p][s]=(word,mp[p][s])

        def check(str1):
            p=ord(str1[0])-97
            s=ord(str1[-1])-97

            node=mp[p][s]
            ans=0
            while node:
                if node[0].startswith(str1) and node[0].endswith(str1):
                    ans+=freq[node[0]]
                node=node[1]
            return ans
        ans=0

        for word in words[::-1]:
            ans+=check(word)
            add(word)
        return ans
            


        