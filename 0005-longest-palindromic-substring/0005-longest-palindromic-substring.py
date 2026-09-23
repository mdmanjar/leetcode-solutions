class Solution:
    def longestPalindrome(self, s: str) -> str:

        start=0
        length=0

        def pol(left,right):
            nonlocal length,start
            if (len(s)-right)*2<length:return

            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1

            left+=1
            right-=1

            x=right-left+1

            if length<x:

                length=x
                start=left
        
        for i in range(len(s)):

            pol(i,i)
            pol(i,i+1)
        
        return s[start:start+length]

        