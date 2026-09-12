class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.countPalindrome(s, i, i) #odd case => left = right = i
            result += self.countPalindrome(s, i, i+1)#even case => left = i & right = i+1
        return result

    def countPalindrome(self, s, left, right):
        count = 0
        length = len(s)
        while left >= 0 and right < length and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

'''
Time:
O(n) - we are starting at each char and expanding pointers
O(n) - doing the same thing for every single character
so n*n
Overall - O(N^2)
'''
        