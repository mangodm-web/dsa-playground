function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let maxArea = 0;
  
  while (left <= right) {
    const newArea = (right - left) * Math.min(height[left], height[right]);
    maxArea = Math.max(maxArea, newArea);
    
    if (height[left] > height[right]) {
      right--;
    } else {
      left++;
    }
  }
  
  return maxArea;
};
