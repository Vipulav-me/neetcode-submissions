class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mul_1(num1,digit):
            ans = 0
            carry = 1
            digit = ord(digit)-ord('0')
            for dig in num1[::-1]:
                dig = (ord(dig)-ord('0'))*carry
                ans += dig*digit
                carry *= 10
            return ans
        car = 1
        ans = 0
        for digit in num2[::-1]:
            ans += mul_1(num1,digit)*car
            car*=10
        def int_to_str(num):
            s = []
            while True:
                s.append(chr(ord('0') + num % 10))
                num //= 10
                if num == 0:
                    break
            return ''.join(reversed(s))
        return int_to_str(ans)