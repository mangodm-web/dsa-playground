class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) + 1):
                if (j - i <= len(result)):
                    continue
                
                if self.is_palindrome(s[i:j]) and j - i > len(result):
                    result = s[i:j]
        
        return result
