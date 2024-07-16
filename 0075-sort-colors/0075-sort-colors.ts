/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
  let [left, current, right] = [0, 0, nums.length - 1];

  while (current <= right) {
    if (nums[current] === 0) {
      [nums[left], nums[current]] = [nums[current], nums[left]];
      left += 1;
      current += 1;
    } else if (nums[current] === 2) {
      [nums[current], nums[right]] = [nums[right], nums[current]];
      right -= 1;
    } else {
      current += 1;
    }
  }
}
