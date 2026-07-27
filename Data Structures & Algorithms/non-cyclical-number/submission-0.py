class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = []
        def sq(num):
            lst = [(int(x))**2 for x in str(num)]
            return sum(lst)
        while sq(n) not in hashmap:
            m = sq(n)
            if m == 1:
                return True
            else:
                hashmap.append(m)
                n = m
        return False
        
            
        
        
        

