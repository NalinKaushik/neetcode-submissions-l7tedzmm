class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        p = total = 0 
        for i in range(1,n):
            if height[p] < height[i]:
                p = i
        
        mainwall = 0
        for i in range(1,p):
            if height[i] > height[mainwall]:
                mainwall = i
            else:
                total += height[mainwall] - height[i]
        
        mainwall = n-1
        for i in range(mainwall - 1,p,-1):
            if height[i] > height[mainwall]:
                mainwall = i
            else:
                total += height[mainwall] - height[i]
        return total