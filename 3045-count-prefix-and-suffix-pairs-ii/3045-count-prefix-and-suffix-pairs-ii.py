from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = {}
        total_pairs = 0
        
        for word in words:
            t = root
            n = len(word)
            
            # Step 1: Walk down the Trie using pairs of (prefix_char, suffix_char)
            # and count how many valid words ended at each matching prefix-suffix step.
            for i in range(n):
                # Character from the front and corresponding character from the back
                pair = (word[i], word[n - 1 - i])
                
                if pair not in t:
                    break
                t = t[pair]
                
                # If a previously inserted word ended at this exact prefix-suffix length,
                # it means that word is both a prefix and suffix of the current word.
                if 'count' in t:
                    total_pairs += t['count']
            
            # Step 2: Insert the current word into the Trie for future words to match against
            t = root
            for i in range(n):
                pair = (word[i], word[n - 1 - i])
                t = t.setdefault(pair, {})
            
            t['count'] = t.get('count', 0) + 1
            
        return total_pairs

        