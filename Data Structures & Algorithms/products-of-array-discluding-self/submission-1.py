class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = [1]*len(nums)
        prefix[0] = 1
        for i in range(1,len(nums)):
            prefix[i] = nums[i-1]*prefix[i-1]
        suffix = [1]*len(nums)
        suffix[len(nums)-1] = 1
        for j in range(len(nums)-2,-1,-1):
            suffix[j] = nums[j+1]*suffix[j+1]
        output = [x*y for x,y in zip(prefix,suffix)]
        return output



            

        