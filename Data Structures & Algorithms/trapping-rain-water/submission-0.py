class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0]*len(height)
        pre[0] = height[0]
        suf = [0]*len(height)
        suf[n-1] = height[n-1]
        for i in range(1,len(height)):
            pre[i] = max(pre[i-1],height[i])
        for i in range(n-2,-1,-1):
            suf[i] = max(suf[i+1],height[i])
        total = 0
        for i in range(n):
            total+= min(pre[i],suf[i]) - height[i]
        return total
        
        