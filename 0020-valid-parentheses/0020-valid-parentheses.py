class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for e in s:
            if e in '({[':
                if e=='(':stack.append(')')
                elif e=='{':stack.append('}')
                else:stack.append(']')
            else:
                if not stack:return False
                if stack[-1]!=e:
                    return False
                stack.pop()
                
        return len(stack)==0
            
        