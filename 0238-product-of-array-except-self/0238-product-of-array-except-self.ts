function productExceptSelf(nums: number[]): number[] {
  const result = [];

  let product = 1;
  for (let i = 0; i < nums.length; i++) {
    result.push(product);
    product *= nums[i];
  }

  product = 1;
  for (let i = nums.length - 1; i > -1; i--) {
    result[i] *= product;
    product *= nums[i];
  }

  return result;
};
