class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            current_width = right - left
            current_height = min(height[left], height[right])
            result = max(result, current_width * current_height)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result
