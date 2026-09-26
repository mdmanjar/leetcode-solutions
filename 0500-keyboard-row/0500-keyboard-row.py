color = [-1] * 26

for c in "qwertyuiop":
    color[ord(c) - 97] = 1

for c in "asdfghjkl":
    color[ord(c) - 97] = 2

# for c in "zxcvbnm":
#     color[ord(c) - 97] = 3


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []

        def idx(c):
            return ord(c) - (65 if c.isupper() else 97)

        for word in words:
            same_color = True

            for i in range(1, len(word)):
                if color[idx(word[i - 1])] != color[idx(word[i])]:
                    same_color = False
                    break

            if same_color:
                ans.append(word)

        return ans