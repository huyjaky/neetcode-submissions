class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_categories = {}
        for i in nums:
            if i in num_categories:
                num_categories[i] += 1
            else:
                num_categories[i] = 1
        sorted_categories = sorted(num_categories.items(), key=lambda x: x[1], reverse=True)
        return [i[0] for i in sorted_categories[:k]]



