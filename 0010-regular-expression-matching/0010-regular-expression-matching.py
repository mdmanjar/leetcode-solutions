class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If we reached the end of both strings
            if j == len(p):
                return i == len(s)
            
            # Check if the current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # If the next character in pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: skip the '('*')' pair (zero occurrence)
                # Option 2: if first_match is true, use the '*' to match s[i] and stay at pattern j
                memo[(i, j)] = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # Normal match for current characters, move both pointers forward
                memo[(i, j)] = first_match and dfs(i + 1, j + 1)
                
            return memo[(i, j)]
            
        return dfs(0, 0)