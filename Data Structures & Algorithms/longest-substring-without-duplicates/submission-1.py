class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        valid_set = set()
        longest = 0
        while right < len(s):
            if s[right] not in valid_set:
                #add s at right to the set first
                valid_set.add(s[right])
                # print(f'valid set = {valid_set}')
                #increase window by moving right
                # print(f'right = {right}')
                window = (right-left)+1
                # print(f'window = {window}')
                longest = max(longest,window)
                right += 1
                # print(f'longest = {longest}')
            else:
                #remove that character first from s at left
                valid_set.remove(s[left])
                #move left by 1
                left+=1
        return longest

#time -- O(N)
# while loop => O(N) and set lookup at worst can be O(N) otherwise O(1)

        
        