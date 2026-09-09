class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = 1
        prev1 = 1

        for i in range(len(s)):
            current = 0

            if s[i] != "0":
                current += prev1

            if i > 0 and 10 <= int(s[i - 1:i + 1]) <= 26:
                current += prev2

            prev2 = prev1
            prev1 = current

        return prev1