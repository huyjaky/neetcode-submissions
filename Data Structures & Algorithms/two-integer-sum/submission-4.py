class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, i_value in enumerate(nums):
            j_value = target - i_value
            if j_value not in nums:
                continue
            j = nums.index(j_value)
            if i == j: continue
            return sorted([i, j])
