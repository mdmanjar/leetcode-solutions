from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = {}

        def add(word):
            ans = 0
            t = root
            n = len(word)
            for i in range(n):
                pair = (word[i], word[n - i - 1])
                t = t.setdefault(pair, {})
                # Count valid prefix-suffix words that were inserted prior to this one
                if 'count' in t:
                    ans += t['count']
            t['count'] = t.get('count', 0) + 1
            return ans

        # Iterate forward to maintain the i < j constraint correctly
        return sum(add(word) for word in words)

        