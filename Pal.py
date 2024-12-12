class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        normalized = ''.join(char.lower() for char in s if char.isalnum())
        return normalized == normalized[::-1]
