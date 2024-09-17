class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    subsequence[i] = max(subsequence[i], 1 + subsequence[j])

        return max(subsequence)
