from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        n = len(temperatures)
        list1 = [0] * n
        stack.append(0)
        # [30,38,30,36,35,40,28]
        for i in range(1,n):
            ct = temperatures[i]
            if temperatures[stack[-1]]< ct:

                while(stack and temperatures[stack[-1]] < ct):
                    popindex = stack.pop()
                    list1[popindex] = i  - popindex

            stack.append(i)

        return list1