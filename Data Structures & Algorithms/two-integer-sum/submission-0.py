class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}
        for i,num in enumerate(nums):
            diff = target-num
            if diff in dict1:
                return [dict1[diff],i]
            dict1[num] = i
        
        


            

