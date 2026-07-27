class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = [0]*26
        t_freq = [0]*26
        for i in s:
            idx = ord(i)-ord('a')
            s_freq[idx] += 1
        for j in t:
            idx_1 = ord(j)-ord('a')
            t_freq[idx_1] += 1
        return s_freq == t_freq