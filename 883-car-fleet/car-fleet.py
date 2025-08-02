class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Draw a position-time graph and it'd be obvious

        ps = sorted([(p, s) for p, s in zip(position, speed)], reverse=True, key=lambda t : t[0])
        stack = []

        for p, s in ps:
            timeToDest = (target - p) / s
            if not stack or stack[-1] < timeToDest:
                stack.append(timeToDest)
        return len(stack)