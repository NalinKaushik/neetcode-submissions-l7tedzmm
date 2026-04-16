class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        # 1. Initialize pointers at the extremes
        left = 0
        right = len(height) - 1
        
        # 2. Keep track of the maximum heights seen so far from both sides
        left_max = height[left]
        right_max = height[right]
        
        total_water = 0
        
        # 3. Move pointers inward until they meet
        while left < right:
            # If the left side is the bottleneck
            if left_max < right_max:
                left += 1
                # Update the max, or add water if we are in a valley
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
                
            # If the right side is the bottleneck
            else:
                right -= 1
                # Update the max, or add water if we are in a valley
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                
        return total_water