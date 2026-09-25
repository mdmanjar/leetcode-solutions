class Solution:
    def numberToWords(self, num: int) -> str:
        one_ten=('','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen')
        twenty_ninty=('','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety')

        def dfs(num):
            if num>=(d:=10**9):
                a,b=divmod(num,d)
                return f'{dfs(a)} Billion' + (f' {dfs(b)}' if b else '')
            elif num>=(d:=10**6):
                a,b=divmod(num,d)
                return f'{dfs(a)} Million' + (f' {dfs(b)}' if b else '')
            elif num>=(d:=10**3):
                a,b=divmod(num,d)
                return f'{dfs(a)} Thousand' + (f' {dfs(b)}' if b else '')
            elif num>=100:
                a,b=divmod(num,100)
                return f'{dfs(a)} Hundred' + (f' {dfs(b)}' if b else '')
            elif 20<=num<100:
                return f'{twenty_ninty[num//10]}' + (f' {dfs(num%10)}' if num%10 else '')
            else:
                return one_ten[num]

        return 'Zero' if num==0 else dfs(num)