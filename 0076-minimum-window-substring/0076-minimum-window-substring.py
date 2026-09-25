class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n=len(s),len(t)

        if m<n:return ''

        mp=[0]*123

        for c in t:mp[ord(c)]+=1

        count=n

        left=0
        start=-1
        length=inf

        for right,c in enumerate(s):


            if mp[ord(c)]>0:count-=1

            mp[ord(c)]-=1

            while count==0:

                new_length=right-left+1

                if new_length<length:

                    length=new_length

                    start=left

                mp[ord(s[left])]+=1

                if mp[ord(s[left])]>0:
                    count+=1

                left+=1

            if length==n:return s[start:start+length]


        return '' if start==-1 else s[start:start+length]