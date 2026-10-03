class Solution:
    def frequencySort(self, s: str) -> str:

        return ''.join(key*freq for key,freq in sorted(((key,freq) for key,freq in Counter(s).items()),key=lambda x:(-x[1],x[0])))

        