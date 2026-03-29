class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(p, (target - p) / s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []
        for p, t in pairs:
            if not stack or t > stack[-1]:
                stack.append(t)
            else:
                pass
        return len(stack)

     