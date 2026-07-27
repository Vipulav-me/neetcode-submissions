class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1
        lst = []
        for j in range(len(nums)):
            if nums[j]-1 not in hashmap:
                lst.append(nums[j])
        maxi = 0
        for k in lst:
            ans = [k]
            start = k
            while start+1 in hashmap:
                ans.append(start+1)
                start += 1
            maxi = max(maxi,len(ans))
        return maxi
