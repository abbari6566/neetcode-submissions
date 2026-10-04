class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary = f"{n:032b}" #change to binary bits
        binaryStr = str(binary)
        reversedString = '' #reverse the string
        
        for b in range(len(binaryStr)-1, -1, -1):
            reversedString += binaryStr[b]
        
        result = int(reversedString, 2)
        return result


        