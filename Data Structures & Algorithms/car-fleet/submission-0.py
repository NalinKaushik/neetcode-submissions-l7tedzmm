from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(list(zip(position,speed)))
        stack = deque()
        n = len(pair)
        for i in range(n-1,-1,-1):
            distance = pair[i][0] - target
            speed = pair[i][1]
            time = distance/speed

            if stack:
                if stack[-1] > time:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)