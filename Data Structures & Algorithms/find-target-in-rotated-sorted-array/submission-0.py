class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        pivot = l
        def b_search(l,r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid]<target:
                    l = mid+1
                else:
                    r = mid-1
            return -1
        ans = b_search(0,pivot-1)
        if ans!= -1:
            return ans
        return b_search(pivot,len(nums)-1)
        

