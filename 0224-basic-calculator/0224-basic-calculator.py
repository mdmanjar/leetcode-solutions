class Solution:
    def calculate(self, s: str) -> int:
        i=0

        def dfs():
            nonlocal i
            stack=[]
            num=0
            op='+'

            def cal(num,op):
                if op=='+':
                    stack.append(num)
                else:
                    stack.append(-num)

            while i<len(s):
                c=s[i]

                if c==' ':
                    i+=1
                    continue

                if c.isdigit():
                    num=num*10+int(c)

                elif c=='(':
                    i+=1
                    num=dfs()
                    i-=1

                elif c in ('+','-'):
                    cal(num,op)
                    op=c
                    num=0

                elif c==')':
                    cal(num,op)
                    i+=1
                    return sum(stack)

                i+=1

            cal(num,op)
            return sum(stack)

        return dfs()


        