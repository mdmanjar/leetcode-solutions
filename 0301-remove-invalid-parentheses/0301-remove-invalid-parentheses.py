class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def valid(s):
            stack=0
            remove=0

            for c in s:
                if c=='(':
                    stack+=1
                elif c==')':
                    if stack:
                        stack-=1
                    else:
                        remove+=1

            return stack+remove

        temp=[]
        ans=set()

        def dfs(i,open,remove):
            if i==len(s):
                if open==0 and remove==0:
                    ans.add(''.join(temp))
                return

            c=s[i]

            if c.isalpha():
                temp.append(c)
                dfs(i+1,open,remove)
                temp.pop()
                return

            if remove>0:
                dfs(i+1,open,remove-1)

            if c=='(':
                temp.append(c)
                dfs(i+1,open+1,remove)
                temp.pop()
            else:
                if open>0:
                    temp.append(c)
                    dfs(i+1,open-1,remove)
                    temp.pop()

        dfs(0,0,valid(s))
        return list(ans)