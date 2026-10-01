class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        mp={}
        most_common=1

        for i,response in enumerate(responses):
            for word in response:
                if word not in mp:
                    mp[word]=(1,i)
                elif mp[word][1]!=i:
                    count=mp[word][0]+1
                    mp[word]=(count,i)
                    most_common=max(most_common,count)
        ans=None
        for key,val in mp.items():
            if val[0]==most_common:
                if ans is None or ans>key:
                    ans=key
        return ans



        
        