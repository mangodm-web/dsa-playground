function maxArea(height: number[]): number {
  let result = 0;
  let left = 0;
  let right = height.length - 1;
  
  
  while (left <= right) {
    const newArea = (right - left) * Math.min(height[left], height[right]);
    result = Math.max(result, newArea);
    
    if (height[left] > height[right]) {
      right--;
    } else {
      left++;
    }
  }
  
  return result;
};
