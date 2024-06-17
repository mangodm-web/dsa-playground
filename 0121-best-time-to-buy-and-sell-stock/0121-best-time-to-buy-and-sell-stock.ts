function maxProfit(prices: number[]): number {
  let result = 0;
  let minPrice = prices[0];
  
  for (let i = 1; i < prices.length; i++) {
    const profit = prices[i] - minPrice;
    
    result = Math.max(result, profit);
    minPrice = Math.min(minPrice, prices[i]);
  }
  
  return result;
};
