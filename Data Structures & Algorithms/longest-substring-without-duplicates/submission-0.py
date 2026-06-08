class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        result = set()
        n = len(s)
        for right in range(n):
            #for invalid window
            while s[right] in result:
                result.remove(s[left])
                left += 1
            longest = max(longest, right-left+1)
            result.add(s[right])
        return longest
        
        