class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [word for word, f in sorted(Counter(words).items(),key=lambda x: (-x[1], x[0]))[:k]]