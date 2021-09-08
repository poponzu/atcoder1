# https://snuke.hatenablog.com/entry/2014/12/02/235837

class Solution:
    def longestPalindrome(self, s: str) -> str:
        MaxL = 0
        ans = ""
        if len(s) == 1:
            return s

        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                partS = s[i:j+1]
                revS = partS[::-1]
                if partS == revS and len(partS) > MaxL:
                    ans = partS
                    # update the length of Longest Palindromic Substring
                    MaxL = len(ans)

        return ans

S = "bb"
solve = Solution()
print(solve.longestPalindrome(S))