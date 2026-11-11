class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):return ''
        if len(s)==len(t) and s==t:return s
        mp=[0]*128

        for e in t:mp[ord(e)]+=1
        count=len(t)
        left=0
        minLen=inf
        start=-1


        for right,e in enumerate(s):
            if mp[ord(e)]>0:count-=1
            mp[ord(e)]-=1

            while count==0:
                if right-left+1<minLen:
                    minLen=right-left+1
                    start=left
                if mp[ord(s[left])]>=0:count+=1
                mp[ord(s[left])]+=1
                left+=1

            
        return s[start:minLen+start] if start!=-1 else ''
        