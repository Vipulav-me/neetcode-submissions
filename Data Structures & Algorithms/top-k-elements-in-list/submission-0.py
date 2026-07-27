class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       from collections import Counter
       arr = Counter(nums)
       return [item[0] for item in arr.most_common(k)]