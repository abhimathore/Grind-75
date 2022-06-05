class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        closing = [']','}',')']
        stack = []
        
        for i in s:
            if i in brackets:
                stack.append(brackets[i])
            elif i in closing:
                if not stack or stack.pop() !=i:
                    return False
        return len(stack) == 0