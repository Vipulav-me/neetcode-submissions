class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n<0:
            n = abs(n)
            for i in range(n):
                ans *= x
            return 1/ans
        else:
            for i in range(n):
                ans *= x
            return ans