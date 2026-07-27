class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            ans = max(ans,r-l+1)
        return ans 