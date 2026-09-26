from string import ascii_lowercase as chars

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        mp=Counter(s)
        left=[]
        right=[]

        mid=None

        for c in chars:
            left.append(c*(mp[c]//2))
            right.append(c*(mp[c]//2))
            mp[c]%=2

            if mp[c]:
                mid=c
        if mid:
            right.append(mid)
        return ''.join(left)+''.join(right[::-1])

        