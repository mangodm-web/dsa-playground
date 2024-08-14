class Solution:    
    def dfs(self, index: int, cum_sum: int, target: int, nums: List[int]) -> bool:
        if cum_sum > target or index == len(nums):
            return False
        
        if cum_sum == target:
            return True
        
        include = self.dfs(index + 1, cum_sum + nums[index], target, nums)
        exclude = self.dfs(index + 1, cum_sum, target, nums)
        
        return include or exclude

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        return self.dfs(0, 0, target, nums)
