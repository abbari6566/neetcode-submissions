class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(",
            "}":"{",
            "]":"["
        }
        stk = []
        for c in s:
            if c not in mapping:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != mapping[c]:
                        return False
        return not stk  
    #time - O(n) 
        