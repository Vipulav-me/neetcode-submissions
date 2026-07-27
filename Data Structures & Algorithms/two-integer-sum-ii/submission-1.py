class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for k in range(n):
            diff = target-numbers[k]
            i = 0
            j = n-1
            while i<=j:
                mid = (i+j)//2
                if numbers[mid] == diff and mid != k:
                    return [min(k,mid)+1,max(k,mid)+1]
                elif numbers[mid] > diff:
                    j = mid-1
                else:
                    i = mid+1 
        