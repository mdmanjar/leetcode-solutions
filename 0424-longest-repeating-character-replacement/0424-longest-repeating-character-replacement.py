class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        mp = [0] * 26
        left = 0
        max_freq = 0  # Tracks the maximum frequency of any character in the current window

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            mp[idx] += 1
            max_freq = max(max_freq, mp[idx])  # Update max frequency

            # If replacements needed exceed k, shrink the window from the left
            while (right - left + 1) - max_freq > k:
                mp[ord(s[left]) - ord('A')] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans