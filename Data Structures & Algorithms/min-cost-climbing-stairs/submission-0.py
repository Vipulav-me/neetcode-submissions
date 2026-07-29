class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1]*len(cost)
        def answer(idx):
            if idx >= len(cost):
                return 0
            if memo[idx] != -1:
                return memo[idx]
            memo[idx] = cost[idx] +min(answer(idx+1),answer(idx+2))
            return memo[idx]
        return min(answer(0),answer(1))

