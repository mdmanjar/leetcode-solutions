class Solution:
    def calculate(self, s: str) -> int:
        i=0


        def dfs():
            nonlocal i
            a=b=0
            sign='+'
            cal=lambda a,b,op:a+b if op=='+' else a-b

            while i<len(s):
                c=s[i]

                if c.isdigit():
                    b=b*10+(ord(c)-48)
                    i+=1
                elif c in ('+','-'):
                    a,b=cal(a,b,sign),0
                    sign=c
                    i+=1
                elif c=='(':
                    i+=1
                    a,b=cal(cal(a,b,sign),dfs(),sign),0
                elif c==')':
                    i+=1
                    return cal(a,b,sign)
                else:
                  i+=1

            return cal(a,b,sign)
        return dfs()