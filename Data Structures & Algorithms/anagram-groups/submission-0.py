class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        if len(strs) == 1:
            return [strs]
        result  = defaultdict(list)
        for word in strs:
            arr = [0]*26
            for char in word:
                idx = ord(char)-ord('a')
                arr[idx] += 1
            result[tuple(arr)].append(word)
        return [v for v in result.values()]
            

        
    
        
        

        