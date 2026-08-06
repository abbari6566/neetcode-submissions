from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        t1 = Counter(t)
        if s1 == t1:
            return True
        else:
            return False
'''
Time:
- to make s1 check every character in s, so O(N) where N is the num of chars
- to make t1 check every character in t, so O(M) where M is the num of chars
- to compare s1 == t1 is O(1) since s and t are only lowercase English letters
  so at max can be O(26)
- overall => O(N+M) or O(N) if s and t are equal in length
''' 