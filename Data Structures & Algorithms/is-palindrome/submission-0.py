class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s1 = ''
        s2 = ''

        for char in s:
            if char.isalnum():
                s1 += char.lower()
        for char in s1[::-1]:
            s2 += char
        
        for p,q in zip(s1,s2):
            if p != q:
                return False
        return True
        