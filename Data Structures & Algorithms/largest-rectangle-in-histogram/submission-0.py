from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = deque()
        area = maxarea = 0

        for i in range(n):
            currh = heights[i]
            popi = i
            while(stack and stack[-1][0] > currh):
                poph , popi = stack.pop()
                area = poph * (i - popi)
                maxarea = max(maxarea,area)
            stack.append((currh, popi))
        
        while stack:
            poph, popi = stack.pop()
            area = poph * (n - popi)
            maxarea = max(maxarea, area)
        return maxarea