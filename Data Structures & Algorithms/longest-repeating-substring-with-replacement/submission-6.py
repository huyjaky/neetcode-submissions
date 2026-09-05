class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26

        left = 0
        max_freq = 0
        longest_substring = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index] += 1

            max_freq = max(max_freq, count[index])

            window_length = right - left + 1

            replacements = window_length - max_freq

            if replacements > k:
                left_index = ord(s[left]) - ord('A')
                count[left_index] -= 1
                left += 1

            longest_substring = max(
                longest_substring,
                right - left + 1
            )

        return longest_substring