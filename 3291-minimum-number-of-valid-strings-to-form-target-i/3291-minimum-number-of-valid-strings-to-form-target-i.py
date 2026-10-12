class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        def is_valid(pre: str) -> bool:
            for word in words:
                if word.startswith(pre):
                    return True
            return False

        n = len(target)
        count = [0] * (n + 1)
        i = 0
        j = 1
        
        while j <= n:
            if i == j:
                return -1
            elif is_valid(target[i:j]):
                count[j] = count[i] + 1
                j += 1
            else:
                i += 1
                
        return count[n]