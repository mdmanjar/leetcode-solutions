class Solution:
    def smallestPalindrome(self, s: str) -> str:
        mp=[0]*26

        for c in s:mp[ord(c)-ord('a')]+=1
        left=[]
        right=[]
        mid=-1
        for i in range(26):
            if mp[i]:
                left.append(chr(i+97)*(mp[i]//2))
                right.append(chr(i+97)*(mp[i]//2))

                if mp[i]%2:mid=i
        if mid!=-1:
            left.append(chr(mid+97))
        return ''.join(left+right[::-1])
            

        