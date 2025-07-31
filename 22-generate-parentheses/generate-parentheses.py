class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def createParenthesis(openRemaining, closeRemaining):
            if openRemaining == closeRemaining == 0:
                res.append("".join(stack))
                return
            if openRemaining > 0:
                stack.append('(')
                createParenthesis(openRemaining - 1, closeRemaining)
                stack.pop()
            if closeRemaining > openRemaining:
                stack.append(')')
                createParenthesis(openRemaining, closeRemaining - 1)
                stack.pop()               
        
        createParenthesis(n, n)
        return res