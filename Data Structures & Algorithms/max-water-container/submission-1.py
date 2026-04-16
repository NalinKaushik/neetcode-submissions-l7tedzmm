class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        p1 = 0
        p2 = n-1
        length = 0
        maxarea = 0
        while(p1<p2):
            val1 = heights[p1]
            val2 = heights[p2]
            length = p2 - p1
            area = min(val1,val2) * length
            maxarea = max(maxarea,area)
            if val1<val2:
                p1+=1
            else:
                p2-=1
        return maxarea