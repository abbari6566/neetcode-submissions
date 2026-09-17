class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initially thought wordDict is a hashmap {}
        # issue found: wordDict is not a dict it is an array so double loop needed
        #Greedy approach I tried didn't work
        # string = ""
        # for char in s:
        #     string += char
        #     for word in wordDict:
        #         print(word, string)
        #         if string == word:
        #             string = ""
        
        # #at the end if string is still empty means we matched all word
        # if len(string) == 0: return True
        # else: return False
        wordSet = set(wordDict)
        maxLen = max(len(word) for word in wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for c1 in range(1, len(s) + 1):
            for c2 in range(c1 - 1, max(-1, c1 - maxLen - 1), -1):
                if dp[c2] and (s[c2:c1] in wordSet):
                    dp[c1] = True
                    break

        return dp[len(s)]
        
'''
Let n = len(s), m = maxLen, and k = len(wordDict).

Time: O(n · m²), plus O(k · m) to build the set.

The outer loop runs n times, once per cut c1.
The inner loop runs at most m times, once per word length up to maxLen.
Inside, s[c2:c1] creates a new string of length up to m, and checking it in the set means hashing that string, which is also O(m).

So you get n × m × m. Building wordSet and finding maxLen walks every character of every word once, which is O(k · m).
'''

            
                 
            

        