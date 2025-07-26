class Solution:
    def isValid(self, s: str) -> bool:
        match = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in match.keys():
                stack.append(c)
            elif len(stack) == 0 or match[stack[-1]] != c:
                return False
            else: stack.pop(-1)
            
            
        return len(stack) == 0
        