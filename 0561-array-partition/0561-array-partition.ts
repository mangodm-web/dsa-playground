function arrayPairSum(nums: number[]): number {
  nums.sort((a, b) => a - b);
  let result = 0;

  for (let i = 0; i < Math.floor(nums.length / 2); i++) {
    result += Math.min(nums[2 * i], nums[2 * i + 1]);
  }

  return result;
};
