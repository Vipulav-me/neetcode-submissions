class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        n = len(nums)
        for i in range(len(nums)):
            target = -nums[i]
            j = i+1
            k = n-1
            while j<k:
                if nums[j]+nums[k] == target:
                    final.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j]+nums[k] > target:
                    k-=1
                else:
                    j+=1
        return [list(t) for t in set(map(tuple,final))]
        

