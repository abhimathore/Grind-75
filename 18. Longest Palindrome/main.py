from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = Counter(s)
        count = 0
        odd = 0
        for i in a:
            if a[i] %2 ==0:
                count = count + a[i]
            else:
                odd = 1
                count = count + a[i] -1
        return count + odd