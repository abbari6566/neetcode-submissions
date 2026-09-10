class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        resLen = 0
        for i in range(len(s)):
            #for odd length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right - left + 1
                if (length) > resLen:
                    resLen = length
                    result = s[left : right+1]
                left -= 1
                right += 1
            
            #for even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right - left + 1
                if (length) > resLen:
                    resLen = length
                    result = s[left : right+1]
                left -= 1
                right += 1
        return result

#Time - O(N^2)


