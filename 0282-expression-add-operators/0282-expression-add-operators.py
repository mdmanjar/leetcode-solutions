class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans=[]

        def dfs(i,currVal,prev,sb):
            if i==len(num):
                if currVal==target:
                    ans.append(''.join(sb))
                return

            number=0
            for j in range(i,len(num)):
                if j>i and num[i]=='0':
                    break

                number=number*10+int(num[j])

                if i==0:
                    sb.append(str(number))
                    dfs(j+1,number,number,sb)
                    sb.pop()
                else:
                    sb.append('+')
                    sb.append(str(number))
                    dfs(j+1,currVal+number,number,sb)
                    sb.pop()
                    sb.pop()

                    sb.append('-')
                    sb.append(str(number))
                    dfs(j+1,currVal-number,-number,sb)
                    sb.pop()
                    sb.pop()

                    sb.append('*')
                    sb.append(str(number))
                    dfs(j+1,currVal-prev+prev*number,prev*number,sb)
                    sb.pop()
                    sb.pop()

        dfs(0,0,0,[])
        return ans