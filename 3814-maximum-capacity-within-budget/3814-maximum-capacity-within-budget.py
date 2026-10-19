from typing import List
import bisect

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)
        # Pair costs and capacities together and sort by cost
        cost_capacity = sorted(zip(costs, capacity))
        
        # Precompute the prefix maximum capacity up to each index
        best_capacity = [0] * n
        best_capacity[0] = cost_capacity[0][1]
        for i in range(1, n):
            best_capacity[i] = max(best_capacity[i - 1], cost_capacity[i][1])
            
        # Extract all costs into a separate list once (O(N) time)
        sorted_costs = [item[0] for item in cost_capacity]
        
        ans = 0
        
        # Consider single items within budget
        for cost, cap in cost_capacity:
            if cost < budget:
                ans = max(ans, cap)
                
        # Consider pairs of items using binary search in O(log N) per iteration
        for i in range(1, n):
            remaining = budget - cost_capacity[i][0] - 1
            if remaining <= 0:
                continue
                
            # Search only in the valid prefix range [0, i - 1] using the 'hi' parameter
            idx = bisect.bisect_right(sorted_costs, remaining, hi=i) - 1
            
            if idx >= 0:
                ans = max(ans, cost_capacity[i][1] + best_capacity[idx])
                
        return ans