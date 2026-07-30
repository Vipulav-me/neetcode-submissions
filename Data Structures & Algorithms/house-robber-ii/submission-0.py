class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        arr1 = nums[:-1]
        arr2 = nums[1:]
        def ans(arr):
            memo = [-1]*len(arr)
            def dfs(i,arr):
                if i>=len(arr):
                    return 0
                if memo[i] != -1:
                    return memo[i]
                memo[i] = max(arr[i]+dfs(i+2,arr),dfs(i+1,arr))
                return memo[i]
            return dfs(0,arr)
        return max(ans(arr1),ans(arr2))
        
        