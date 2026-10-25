import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #operators - [+,-,*,/]

        stack = []

        for tok in tokens:
            if tok in "+-*/":
                #b = 1st most recent, a the 2nd most recent
                b, a = stack.pop(), stack.pop()
                
                if tok == "+":
                    stack.append(a+b)
                
                elif tok == "-":
                    stack.append(a-b)

                elif tok == "*":
                    stack.append(a*b)
                
                else:
                    division = a / b
                    if division < 0:
                        stack.append(math.ceil(division))
                    else:
                        stack.append(math.floor(division))
            else:
                stack.append(int(tok))   
        return stack[0]

#time - O(n) #length of tokens
#space - O(n)
            
                

                
        