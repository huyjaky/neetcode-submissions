class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, total):
            # Đã đạt target
            if total == target:
                result.append(current.copy())
                return

            # Vượt target
            if total > target:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])

                # i thay vì i + 1
                # vì được phép dùng lại nums[i]
                backtrack(i, current, total + nums[i])

                # quay lui
                current.pop()

        backtrack(0, [], 0)

        return result