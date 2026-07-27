class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        start = 1
        end = max_pile
        result = end
        while start<=end:
            mid = (start+end)//2
            time = 0
            for p in piles:
                time+= math.ceil(float(p)/mid)
            if time <=h:
                result = mid
                end = mid-1
            else:
                start = mid+1
        return result
