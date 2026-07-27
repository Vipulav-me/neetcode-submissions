class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch == ')':
                if not stack or stack.pop()!='(':
                    return False
            elif ch == '}':
                if not stack or stack.pop()!='{':
                    return False
            elif ch == ']':
                if not stack or stack.pop()!='[':
                    return False
        return len(stack)==0
            

        