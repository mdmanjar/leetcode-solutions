class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def one_word():
            last = ' '.join(temp)
            ans.append(last + ' ' * (maxWidth - len(last)))

        def more_word():
            gap=len(temp)-1
            space=maxWidth-(length)
            each=space//gap
            extra=space%gap

            x = []

            for i, word in enumerate(temp):
                x.append(word)

                if i < gap:
                    x.append(
                        ' ' * (each + (1 if i < extra else 0))
                    )

            ans.append(''.join(x))



        temp=[]
        length=0
        ans=[]

        for word in words:
            if length+len(temp)+len(word)>maxWidth:
                if len(temp)==1:one_word()
                else:more_word()
                temp.clear()
                length=0
            length+=len(word)
            temp.append(word)
        
        one_word()
        
        return ans
            
        