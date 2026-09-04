class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        memory = []
        count = 0
        for i in range(len(nums)):
            if i == len(nums)-1:
                memory.append(count)
                break
            if -1*(nums[i] - nums[i+1]) == 1:
                count += 1
            else: 
                memory.append(count)
                count = 0
        return max(memory) + 1 if memory else 0
