import heapq
import math
from typing import List

class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        # dist[i][j][parity] where parity 0 means next action is even, 1 means next action is odd
        dist = [[[math.inf] * 2 for _ in range(n)] for _ in range(m)]
        
        # Priority queue elements: (cost, r, c, parity)
        # Start at (0, 0) with initial cost 1. 
        # The problem states: "Actions performed after entering (0, 0) are numbered starting from 1."
        # Action 1 is odd-numbered, so required parity for the *next* move is odd (1).
        hp = [(1, 0, 0, 1)]
        dist[0][0][1] = 1
        
        dirs_odd = ((0, 1), (1, 0))   # Right, Down (allowed on odd-numbered actions)
        dirs_even = ((0, -1), (-1, 0)) # Left, Up (allowed on even-numbered actions)
        all_dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        while hp:
            d, r, c, parity = heapq.heappop(hp)
            
            if (r, c) == (m - 1, n - 1):
                return d
                
            if d > dist[r][c][parity]:
                continue
                
            # Option 1: Wait at the current cell
            # Waiting costs penalty[r][c] and flips the parity
            wait_cost = d + penalty[r][c]
            next_parity_wait = 1 - parity
            if wait_cost < dist[r][c][next_parity_wait]:
                dist[r][c][next_parity_wait] = wait_cost
                heapq.heappush(hp, (wait_cost, r, c, next_parity_wait))

            # Option 2: Move to adjacent cells
            valid_rule_dirs = dirs_odd if parity == 1 else dirs_even
            
            for dr, dc in all_dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    entry_cost = (nr + 1) * (nc + 1)
                    
                    # Check if the move follows the parity rule
                    is_valid_move = (dr, dc) in valid_rule_dirs
                    
                    extra_cost = 0 if is_valid_move else penalty[r][c]
                    new_d = d + entry_cost + extra_cost
                    next_parity_move = 1 - parity
                    
                    if new_d < dist[nr][nc][next_parity_move]:
                        dist[nr][nc][next_parity_move] = new_d
                        heapq.heappush(hp, (new_d, nr, nc, next_parity_move))
                        
        return -1