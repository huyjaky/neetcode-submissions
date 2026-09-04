class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        # Check if the cleaned string is equal to its reverse
        return cleaned_s == cleaned_s[::-1]

        
