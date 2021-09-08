class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        # so I want to create frames of different lengths
        # that will move along a string
        # so if string is abba
        # the first frame is abba
        # the second iteration be: abb, bba
        # third iteration be: ab, bb, ba
        # we start with widest frame, because we are after longest
        # palindromic substring
        # right off the bat check if the input itself is a non empty palindromic string
        if not s:
            raise Exception("You weren't supposed to be null")

        if self.isPalindrome(s):
            return s

        for i in range(len(s), 0, -1):
            for j in range(0, len(s)-i+1):
                candidate = s[j:j+i]
                if self.isPalindrome(candidate):
                    return candidate


solve = Solution()
S = "abbac"
print(solve.longestPalindrome(S))