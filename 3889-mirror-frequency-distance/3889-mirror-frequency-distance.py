class Solution:
    def mirrorFrequency(self, s: str) -> int:
        mp = [0] * 128
        ans = 0
        
        # First pass: count frequencies
        for e in s:
            mp[ord(e)] += 1
            
        # Second pass: compute the mirror difference
        for e in s:
            # Skip if already processed/cleared
            if mp[ord(e)] == 0:
                continue
                
            if e.isdigit():
                val = ord(e) - 48
                mirror_val = 9 - val
                m_char = chr(mirror_val + 48)
            else:
                val = ord(e) - 97
                mirror_val = 25 - val
                m_char = chr(mirror_val + 97)
                
            ans += abs(mp[ord(e)] - mp[ord(m_char)])
            
            # Clear frequencies to avoid recounting the same pair
            mp[ord(e)] = 0
            mp[ord(m_char)] = 0
            
        return ans